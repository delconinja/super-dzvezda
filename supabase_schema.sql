-- ── STUDENTS ─────────────────────────────────────────────────────
CREATE TABLE students (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  parent_id     UUID REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  name          TEXT NOT NULL,
  grade         INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 9),
  pin           TEXT NOT NULL,
  stars_total   INTEGER DEFAULT 0,
  streak        INTEGER DEFAULT 0,
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

-- ── SUBSCRIPTIONS ─────────────────────────────────────────────────
CREATE TABLE subscriptions (
  id                UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  parent_id         UUID REFERENCES auth.users(id) ON DELETE CASCADE UNIQUE NOT NULL,
  status            TEXT DEFAULT 'trial' CHECK (status IN ('trial','active','expired','cancelled')),
  trial_ends_at     TIMESTAMPTZ NOT NULL,
  subscribed_until  TIMESTAMPTZ,
  created_at        TIMESTAMPTZ DEFAULT NOW()
);

-- ── PROGRESS ──────────────────────────────────────────────────────
CREATE TABLE progress (
  id            UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  student_id    UUID REFERENCES students(id) ON DELETE CASCADE NOT NULL,
  lesson_id     TEXT NOT NULL,
  stars_earned  INTEGER DEFAULT 0 CHECK (stars_earned BETWEEN 0 AND 3),
  completed     BOOLEAN DEFAULT FALSE,
  attempts      INTEGER DEFAULT 1,
  completed_at  TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(student_id, lesson_id)
);

-- ── ROW LEVEL SECURITY ────────────────────────────────────────────
ALTER TABLE students     ENABLE ROW LEVEL SECURITY;
ALTER TABLE subscriptions ENABLE ROW LEVEL SECURITY;
ALTER TABLE progress     ENABLE ROW LEVEL SECURITY;

-- Parents can only see/edit their own students
CREATE POLICY "parent_own_students" ON students
  USING (parent_id = auth.uid());

CREATE POLICY "parent_insert_students" ON students
  FOR INSERT WITH CHECK (parent_id = auth.uid());

CREATE POLICY "parent_update_students" ON students
  FOR UPDATE USING (parent_id = auth.uid());

-- Parents can only see their own subscription
CREATE POLICY "parent_own_subscription" ON subscriptions
  USING (parent_id = auth.uid());

CREATE POLICY "parent_insert_subscription" ON subscriptions
  FOR INSERT WITH CHECK (parent_id = auth.uid());

-- Progress: accessible by the parent who owns the student
CREATE POLICY "parent_student_progress" ON progress
  USING (
    student_id IN (
      SELECT id FROM students WHERE parent_id = auth.uid()
    )
  );

CREATE POLICY "parent_insert_progress" ON progress
  FOR INSERT WITH CHECK (
    student_id IN (
      SELECT id FROM students WHERE parent_id = auth.uid()
    )
  );

CREATE POLICY "parent_update_progress" ON progress
  FOR UPDATE USING (
    student_id IN (
      SELECT id FROM students WHERE parent_id = auth.uid()
    )
  );
