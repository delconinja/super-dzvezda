import { NextRequest, NextResponse } from 'next/server'

const VOICE_ID = 'pNInz6obpgDQGcFmaJgB' // Adam — ElevenLabs multilingual voice

export async function POST(req: NextRequest) {
  if (!process.env.ELEVENLABS_API_KEY) {
    return NextResponse.json({ error: 'TTS not configured' }, { status: 503 })
  }

  const { text } = await req.json()
  if (!text) return NextResponse.json({ error: 'No text' }, { status: 400 })

  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`, {
    method: 'POST',
    headers: {
      'xi-api-key': process.env.ELEVENLABS_API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    }),
  })

  if (!res.ok) {
    return NextResponse.json({ error: 'ElevenLabs error' }, { status: 500 })
  }

  const audio = await res.arrayBuffer()
  return new NextResponse(audio, {
    headers: { 'Content-Type': 'audio/mpeg', 'Cache-Control': 'public, max-age=86400' },
  })
}
