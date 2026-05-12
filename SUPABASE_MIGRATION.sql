-- ============================================================
-- Super Ѕвезда — Supabase Migration
-- Run this once in: Supabase Dashboard → SQL Editor → New query
-- ============================================================

-- 1. Challenge stars (persists yellow/green/blue stars per unit per student)
create table if not exists challenge_stars (
  id         uuid primary key default gen_random_uuid(),
  student_id uuid references students(id) on delete cascade not null,
  unit_id    text not null,
  yellow     boolean default false,
  green      boolean default false,
  blue       boolean default false,
  attempts   int default 0,
  updated_at timestamptz default now(),
  unique(student_id, unit_id)
);

-- 2. User badges (one row per badge earned per student)
create table if not exists user_badges (
  id         uuid primary key default gen_random_uuid(),
  student_id uuid references students(id) on delete cascade not null,
  badge_id   text not null,
  earned_at  timestamptz default now(),
  unique(student_id, badge_id)
);

-- 3. Enable row level security (service role key bypasses this automatically)
alter table challenge_stars enable row level security;
alter table user_badges enable row level security;

-- ============================================================
-- That's it. Once these two tables exist:
--   - Challenge stars save permanently (no more localStorage loss)
--   - 15 badges are awarded automatically after lessons and challenges
--   - Badges appear on student dashboard, parent progress page,
--     and as a pill on each child card in the parent dashboard
-- ============================================================
