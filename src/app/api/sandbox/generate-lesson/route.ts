import { NextRequest, NextResponse } from 'next/server'

// POST /api/sandbox/generate-lesson
// Body: { topic: string, grade: number }
// Returns: InteractiveLessonSpec
//
// Calls OpenAI to produce a 4–5 scene interactive lesson spec in MK,
// using only widget types our runtime supports.
// Subtitles + popup-style narration, no voice yet.

const SYSTEM_PROMPT = `Ти си експерт педагог за основно образование во Северна Македонија.
Твојата задача: за дадена тема од BRO програма, креирај интерактивна лекција од 4 или 5 СЦЕНИ
кои го следат Synthesis-стилот:
  1. Хук — кратка слика што го привлекува вниманието
  2. Градба — детето сам прави нешто
  3. Откривање — преку допир/манипулација детето го открива правилото
  4. Примена — користи го новото знаење на чист пример
  5. Проверка — последна проверка

Правила:
- Сите текстови мора да бидат на македонски јазик (кирилица).
- Користи ги САМО следните типови виџети:
  • "identify" — детето избира еден од 4 визуелни прикажаници (parts + shaded)
  • "tap-shade" — детето допира делови додека не обои target број
  • "splittable-pie" — детето допира парче од пица што се дели на повеќе еднакви парчиња (за еквивалентни дропки)
  • "fraction-pair" — две дропки една до друга

- За шема (shape) можеш да избереш 'bar' (правоаголник) или 'pie' (пица круг).
- АКО темата има врска со пица, торта, делба на парчиња → користи 'pie'.
- АКО темата има врска со линија, лента, мерка → користи 'bar'.

- За СЕКОЈА сцена дај НЕКОЛКУ narration beats (поплучки) кои се прикажуваат како превод:
  - "enter" — кога сцената се отвора (поздрав, прашање)
  - "on-progress" — додека детето работи (охрабрување, навод)
  - "on-success" — кога точно одговори (пофалба + експлицитна врска со учењето)
  - "on-wrong" — кога погрешно (благ поправ)
  - "on-hint" — совет ако грешка повторно

- Тонот: топол, трпелив, охрабрувачки. Како најдобар учител 1-на-1.
- Сите дропки и броеви морат да бидат педагошки точни и BRO-усогласени.

Врати валиден JSON во точно дадениот формат.`

const RESPONSE_SCHEMA = {
  type: 'object' as const,
  properties: {
    lessonId: { type: 'string' },
    title: { type: 'string' },
    bro_topic: { type: 'string' },
    scenes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          prompt: { type: 'string' },
          hint: { type: 'string' },
          successMessage: { type: 'string' },
          narration: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                trigger: {
                  type: 'string',
                  enum: ['enter', 'on-progress', 'on-success', 'on-wrong', 'on-hint'],
                },
                text: { type: 'string' },
              },
              required: ['trigger', 'text'],
              additionalProperties: false,
            },
          },
          widget: {
            anyOf: [
              {
                type: 'object',
                properties: {
                  type: { type: 'string', enum: ['identify'] },
                  config: {
                    type: 'object',
                    properties: {
                      question: { type: 'string' },
                      shape: { type: 'string', enum: ['bar', 'pie'] },
                      choices: {
                        type: 'array',
                        items: {
                          type: 'object',
                          properties: {
                            parts: { type: 'number' },
                            shaded: { type: 'number' },
                            isCorrect: { type: 'boolean' },
                          },
                          required: ['parts', 'shaded', 'isCorrect'],
                          additionalProperties: false,
                        },
                      },
                    },
                    required: ['question', 'choices'],
                    additionalProperties: false,
                  },
                },
                required: ['type', 'config'],
                additionalProperties: false,
              },
              {
                type: 'object',
                properties: {
                  type: { type: 'string', enum: ['tap-shade'] },
                  config: {
                    type: 'object',
                    properties: {
                      parts: { type: 'number' },
                      target: { type: 'number' },
                    },
                    required: ['parts', 'target'],
                    additionalProperties: false,
                  },
                },
                required: ['type', 'config'],
                additionalProperties: false,
              },
              {
                type: 'object',
                properties: {
                  type: { type: 'string', enum: ['splittable-pie'] },
                  config: {
                    type: 'object',
                    properties: {
                      startParts: { type: 'number' },
                      startShaded: { type: 'number' },
                      finalParts: { type: 'number' },
                      compareTo: {
                        type: 'object',
                        properties: {
                          parts: { type: 'number' },
                          shaded: { type: 'number' },
                        },
                        required: ['parts', 'shaded'],
                        additionalProperties: false,
                      },
                    },
                    required: ['startParts', 'startShaded', 'finalParts'],
                    additionalProperties: false,
                  },
                },
                required: ['type', 'config'],
                additionalProperties: false,
              },
              {
                type: 'object',
                properties: {
                  type: { type: 'string', enum: ['fraction-pair'] },
                  config: {
                    type: 'object',
                    properties: {
                      left: {
                        type: 'object',
                        properties: { parts: { type: 'number' }, shaded: { type: 'number' } },
                        required: ['parts', 'shaded'],
                        additionalProperties: false,
                      },
                      right: {
                        type: 'object',
                        properties: { parts: { type: 'number' }, shaded: { type: 'number' } },
                        required: ['parts', 'shaded'],
                        additionalProperties: false,
                      },
                    },
                    required: ['left', 'right'],
                    additionalProperties: false,
                  },
                },
                required: ['type', 'config'],
                additionalProperties: false,
              },
            ],
          },
        },
        required: ['id', 'narration', 'widget'],
        additionalProperties: false,
      },
    },
  },
  required: ['lessonId', 'title', 'bro_topic', 'scenes'],
  additionalProperties: false,
}

export async function POST(req: NextRequest) {
  const key = process.env.OPENAI_API_KEY
  if (!key) {
    return NextResponse.json({ error: 'OPENAI_API_KEY not set' }, { status: 500 })
  }

  const body = await req.json().catch(() => null)
  if (!body || typeof body.topic !== 'string') {
    return NextResponse.json({ error: 'Missing topic' }, { status: 400 })
  }
  const grade = typeof body.grade === 'number' ? body.grade : 6
  const userPrompt = `Тема: ${body.topic}\nОдделение: ${grade}\n\nГенерирај интерактивна лекција со 4–5 сцени според правилата.`

  const apiBody = {
    model: 'gpt-5',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
    ],
    response_format: {
      type: 'json_schema',
      json_schema: {
        name: 'InteractiveLessonSpec',
        strict: false,
        schema: RESPONSE_SCHEMA,
      },
    },
    temperature: 0.7,
  }

  try {
    const r = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${key}`,
      },
      body: JSON.stringify(apiBody),
    })

    if (!r.ok) {
      const errText = await r.text()
      return NextResponse.json(
        { error: 'OpenAI error', status: r.status, detail: errText },
        { status: 502 },
      )
    }
    const data = await r.json()
    const content = data.choices?.[0]?.message?.content
    if (!content) {
      return NextResponse.json({ error: 'No content', raw: data }, { status: 502 })
    }
    let spec
    try {
      spec = JSON.parse(content)
    } catch {
      return NextResponse.json({ error: 'Bad JSON', raw: content }, { status: 502 })
    }
    return NextResponse.json({ spec, usage: data.usage })
  } catch (e: unknown) {
    const msg = e instanceof Error ? e.message : String(e)
    return NextResponse.json({ error: 'Fetch failed', detail: msg }, { status: 500 })
  }
}
