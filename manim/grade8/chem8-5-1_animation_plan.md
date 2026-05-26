# chem8-5-1 — Animation Pacing & Timing

## Pacing Rules (LOCKED)
- Movement every 8-12 seconds (strict)
- No static screens > 12 seconds
- Smooth morphing (never instant jumps)
- Glow/highlight for emphasis

## Timeline
- 0-10s: Hook (emotional engagement)
- 10-30s: Definition (introduce concept)
- 30-90s: Demo (visual explanation)
- 90-150s: Properties (core facts)
- 150-210s: Examples (real-world)
- 210-270s: Comparison (relationships)
- 270-end: Recap (summary)

## Movement Checkpoints
- Every scene: movement_checkpoint(scene, 8-12)
- Equations: animate step by step
- Text: fade in (2s), display, fade out (1s)
- 3D: rotate/zoom smoothly (3-5s)

## Color Consistency
- Primary (Cyan): Main concepts
- Secondary (Green): Energy/positive
- Tertiary (Orange): Forces/vectors
- Highlight (Yellow): Unknowns
- Emphasis (Red): Key points
- Accent (Purple): Special concepts
