import { NextRequest, NextResponse } from 'next/server'
import { createServiceClient } from '@/lib/supabase-server'

export async function GET(req: NextRequest) {
  const studentId = req.nextUrl.searchParams.get('studentId')
  if (!studentId) return NextResponse.json({ error: 'Missing studentId' }, { status: 400 })

  const sb = createServiceClient()
  const { data } = await sb
    .from('user_badges')
    .select('badge_id, earned_at')
    .eq('student_id', studentId)
    .order('earned_at', { ascending: false })

  return NextResponse.json(data || [])
}
