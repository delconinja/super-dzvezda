import { LessonRunner } from '@/components/interactive/LessonRunner'
import { math6_1_5_spec } from '@/lib/interactive/math6-1-5-spec'
import { notFound } from 'next/navigation'
import type { InteractiveLessonSpec } from '@/lib/interactive/types'

const SPECS: Record<string, InteractiveLessonSpec> = {
  'math6-1-5': math6_1_5_spec,
}

interface Props {
  params: Promise<{ lessonId: string }>
}

export default async function InteractiveLessonPage({ params }: Props) {
  const { lessonId } = await params
  const spec = SPECS[lessonId]
  if (!spec) return notFound()
  return <LessonRunner spec={spec} />
}

export function generateStaticParams() {
  return Object.keys(SPECS).map((lessonId) => ({ lessonId }))
}
