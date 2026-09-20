// Reference hand-written interactive lesson spec.
// In production, the OpenAI agent generates these from BRO corpus.

import type { InteractiveLessonSpec } from './types'

export const math6_1_5_spec: InteractiveLessonSpec = {
  lessonId: 'math6-1-5',
  title: 'Дропки',
  bro_topic: 'Дропки, проценти и размер',

  scenes: [
    // 1) HOOK — pizza visual since narration mentions pizza
    {
      id: 's1-hook',
      prompt: 'Која дропка ја прикажува сликата?',
      widget: {
        type: 'identify',
        config: {
          question: 'Колкав дел од пицата е со топинг?',
          shape: 'pie',
          choices: [
            { parts: 4, shaded: 3, isCorrect: true },
            { parts: 4, shaded: 1, isCorrect: false },
            { parts: 4, shaded: 2, isCorrect: false },
            { parts: 4, shaded: 4, isCorrect: false },
          ],
        },
      },
      narration: [
        { trigger: 'enter', text: 'Замисли пица поделена на 4 еднакви парчиња. 3 од нив имаат топинг.' },
        { trigger: 'on-success', text: 'Браво! 3 од 4 парчиња = 3/4. Така ја читаме дропката.' },
        { trigger: 'on-wrong', text: 'Не сосема. Преброј ги парчињата со топинг (горниот број) од вкупно парчиња (долниот).' },
        { trigger: 'on-hint', text: 'Совет: 3 парчиња од 4 значи горе пишуваме 3, долу 4.' },
      ],
      hint: '3 обоени од 4 → 3/4',
    },

    // 2) BUILD — kid shades a bar
    {
      id: 's2-build',
      prompt: 'Обои 2 од 5 парчиња',
      widget: {
        type: 'tap-shade',
        config: { parts: 5, target: 2 },
      },
      narration: [
        { trigger: 'enter', text: 'Сега ти направи дропка. Допри ги парчињата додека не обоиш точно 2 од 5.' },
        { trigger: 'on-progress', text: 'Одлично — обоиш парчиња. Кога ќе имаш 2, притисни „Провери“.' },
        { trigger: 'on-success', text: 'Точно! 2 обоени од вкупно 5 → дропката е 2/5.' },
        { trigger: 'on-wrong', text: 'Не толку. Гледај колку си обоил.' },
        { trigger: 'on-hint', text: 'Совет: треба точно 2 парчиња да светнат пред да притиснеш Провери.' },
      ],
    },

    // 3) DISCOVER — splittable pie. The split IS the proof.
    {
      id: 's3-discover',
      prompt: 'Допри ја половината пица — види што ќе се случи',
      widget: {
        type: 'splittable-pie',
        config: {
          startParts: 2,
          startShaded: 1,
          finalParts: 4,
          compareTo: { parts: 4, shaded: 2 },
        },
      },
      narration: [
        { trigger: 'enter', text: 'Лево гледаш половина пица (1/2). Десно гледаш друга пица. Дали се исти?' },
        { trigger: 'on-progress', text: 'Се дели! Гледај — половината се претвора во 2 парчиња од 4.' },
        { trigger: 'on-success', text: 'Гледаш? 1/2 = 2/4. Истиот дел, различно делен. Тоа се „еквивалентни дропки“.' },
      ],
    },

    // 4) APPLY — reduce 6/9
    {
      id: 's4-apply',
      prompt: 'Која е нескратливата форма на 6/9?',
      widget: {
        type: 'identify',
        config: {
          question: '6/9 во нескратлива форма е:',
          shape: 'bar',
          choices: [
            { parts: 3, shaded: 2, isCorrect: true },
            { parts: 9, shaded: 6, isCorrect: false },
            { parts: 6, shaded: 3, isCorrect: false },
            { parts: 9, shaded: 3, isCorrect: false },
          ],
        },
      },
      narration: [
        { trigger: 'enter', text: 'Скрати ја дропката 6/9. Подели го броителот и именителот со ист број.' },
        { trigger: 'on-success', text: 'Точно! 6/9 = (6÷3)/(9÷3) = 2/3.' },
        { trigger: 'on-wrong', text: 'Не баш. Барај најголем заеднички делител на 6 и 9.' },
        { trigger: 'on-hint', text: 'Совет: и 6 и 9 се деливи со 3.' },
      ],
    },

    // 5) CHECK
    {
      id: 's5-check',
      prompt: 'Која слика покажува 3/4?',
      widget: {
        type: 'identify',
        config: {
          question: 'Избери ја сликата за 3/4:',
          shape: 'pie',
          choices: [
            { parts: 4, shaded: 3, isCorrect: true },
            { parts: 4, shaded: 2, isCorrect: false },
            { parts: 3, shaded: 4, isCorrect: false },
            { parts: 8, shaded: 6, isCorrect: false },
          ],
        },
      },
      narration: [
        { trigger: 'enter', text: 'Последна проверка. Која пица покажува 3/4 со топинг?' },
        { trigger: 'on-success', text: 'Совршено! Готов(а) си со лекцијата. 🎉' },
        { trigger: 'on-wrong', text: 'Скоро! 3/4 значи 3 парчиња топинг од 4 вкупно.' },
        { trigger: 'on-hint', text: 'Совет: горниот број е колку да се обои; долниот е вкупно парчиња.' },
      ],
    },
  ],
}
