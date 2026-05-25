#!/usr/bin/env python3
"""
Render helper for Grade 8 videos.
Usage:
  python render.py                        # list all lessons
  python render.py physics 1 1           # render phys8-1-1
  python render.py math 5 4              # render m8-5-4
  python render.py physics 1 all         # render all lessons in unit 1
  python render.py math all              # render ALL math lessons
  python render.py all                   # render everything

Quality flags (add after lesson args):
  --hq    High quality 1080p60  (manim -qh)
  --lq    Low quality 480p15    (manim -ql, DEFAULT)
  --mq    Medium quality 720p30 (manim -qm)
"""
import subprocess
import sys
import os

LESSONS = {
    "math": {
        1: {
            1: ("m8-1-1.py", "M811Scene", "Цели броеви, степени и корени"),
            2: ("m8-1-2.py", "M812Scene", "Вредност, подредување и заокружување"),
            3: ("m8-1-3.py", "M813Scene", "Дропки, децимални, проценти, размери, пропорции"),
            4: ("m8-1-4.py", "M814Scene", "Математички операции"),
        },
        2: {
            1: ("m8-2-1.py", "M821Scene", "Изрази, равенки и формули"),
            2: ("m8-2-2.py", "M822Scene", "Низи, функции и графици"),
        },
        3: {
            1: ("m8-3-1.py", "M831Scene", "Форми и геометриско размислување"),
            2: ("m8-3-2.py", "M832Scene", "Положба и движење"),
            3: ("m8-3-3.py", "M833Scene", "Плоштина, периметар и зафатнина"),
        },
        4: {
            1: ("m8-4-1.py", "M841Scene", "Должина, маса и зафатнина"),
            2: ("m8-4-2.py", "M842Scene", "Време"),
        },
        5: {
            1: ("m8-5-1.py", "M851Scene", "Планирање и собирање податоци"),
            2: ("m8-5-2.py", "M852Scene", "Обработка и претставување на податоци"),
            3: ("m8-5-3.py", "M853Scene", "Толкување и дискутирање за резултатите"),
            4: ("m8-5-4.py", "M854Scene", "Веројатност"),
        },
    },
    "physics": {
        1: {
            1: ("phys8-1-1.py", "Phys811Scene", "Што прават силите?"),
            2: ("phys8-1-2.py", "Phys812Scene", "Сили и промена на облик"),
            3: ("phys8-1-3.py", "Phys813Scene", "Брзина и пресметки"),
            4: ("phys8-1-4.py", "Phys814Scene", "Графикони растојание-време"),
            5: ("phys8-1-5.py", "Phys815Scene", "Графикони брзина-време и забрзување"),
            6: ("phys8-1-6.py", "Phys816Scene", "Сили и движење"),
            7: ("phys8-1-7.py", "Phys817Scene", "Триење"),
            8: ("phys8-1-8.py", "Phys818Scene", "Гравитација"),
        },
        2: {
            1: ("phys8-2-1.py", "Phys821Scene", "Облици на енергија"),
            2: ("phys8-2-2.py", "Phys822Scene", "Пренесување на енергија"),
            3: ("phys8-2-3.py", "Phys823Scene", "Енергијата во телото"),
            4: ("phys8-2-4.py", "Phys824Scene", "Извори на електрична енергија"),
            5: ("phys8-2-5.py", "Phys825Scene", "Искористување и губење на енергија"),
        },
        3: {
            1: ("phys8-3-1.py", "Phys831Scene", "Само-светлечки и несветлечки предмети"),
            2: ("phys8-3-2.py", "Phys832Scene", "Сенки"),
            3: ("phys8-3-3.py", "Phys833Scene", "Рефлексија и закон за рефлексија"),
            4: ("phys8-3-4.py", "Phys834Scene", "Рефракција (прелом) на светлина"),
            5: ("phys8-3-5.py", "Phys835Scene", "Бои и дисперзија"),
            6: ("phys8-3-6.py", "Phys836Scene", "Леќи и окото — оптика во медицина"),
        },
        4: {
            1: ("phys8-4-1.py", "Phys841Scene", "Ден и ноќ"),
            2: ("phys8-4-2.py", "Phys842Scene", "Годишни времиња"),
            3: ("phys8-4-3.py", "Phys843Scene", "Ѕвезди и планети"),
            4: ("phys8-4-4.py", "Phys844Scene", "Сончевиот систем"),
            5: ("phys8-4-5.py", "Phys845Scene", "Месечина — единствен природен сателит"),
        },
    },
    "chemistry": {
        1: {
            1: ("chem8-1-1.py", "Chem811Scene", "Својства на агрегатните состојби"),
            2: ("chem8-1-2.py", "Chem812Scene", "Промени на агрегатната состојба"),
            3: ("chem8-1-3.py", "Chem813Scene", "Гасен притисок"),
            4: ("chem8-1-4.py", "Chem814Scene", "Дифузија"),
        },
        2: {
            1: ("chem8-2-1.py", "Chem821Scene", "Секојдневни материјали и нивните својства"),
            2: ("chem8-2-2.py", "Chem822Scene", "Споредување материјали"),
            3: ("chem8-2-3.py", "Chem823Scene", "Метали и неметали во периодниот систем"),
            4: ("chem8-2-4.py", "Chem824Scene", "Метали и легури"),
            5: ("chem8-2-5.py", "Chem825Scene", "Периоден систем и групи на елементите"),
        },
        3: {
            1: ("chem8-3-1.py", "Chem831Scene", "Елементи и атоми"),
            2: ("chem8-3-2.py", "Chem832Scene", "Хемиски симболи"),
            3: ("chem8-3-3.py", "Chem833Scene", "Што е соединение?"),
            4: ("chem8-3-4.py", "Chem834Scene", "Хемиски формули"),
            5: ("chem8-3-5.py", "Chem835Scene", "Прости супстанци, соединенија и смеси"),
            6: ("chem8-3-6.py", "Chem836Scene", "Разделување смеси — практични примери"),
        },
        4: {
            1: ("chem8-4-1.py", "Chem841Scene", "Физичка промена или хемиска реакција?"),
            2: ("chem8-4-2.py", "Chem842Scene", "Реактанти, продукти, балансирање равенки"),
            3: ("chem8-4-3.py", "Chem843Scene", "Реакции со кислород — оксиди"),
            4: ("chem8-4-4.py", "Chem844Scene", "Хидроксиди и реакции со вода"),
            5: ("chem8-4-5.py", "Chem845Scene", "Универзален индикатор и pH скала"),
            6: ("chem8-4-6.py", "Chem846Scene", "Реакции на неутрализација"),
            7: ("chem8-4-7.py", "Chem847Scene", "Рѓосување и заштита од корозија"),
            8: ("chem8-4-8.py", "Chem848Scene", "Киселини и бази во секојдневие"),
        },
        5: {
            1: ("chem8-5-1.py", "Chem851Scene", "Вовед во хемијата на јаглеродни соединенија"),
            2: ("chem8-5-2.py", "Chem852Scene", "Алкани и хомологни низи"),
            3: ("chem8-5-3.py", "Chem853Scene", "Фосилни и алтернативни горива"),
            4: ("chem8-5-4.py", "Chem854Scene", "Согорување на горива и животна средина"),
        },
    },
}

# Human-readable subject names (Macedonian)
SUBJECT_LABELS = {
    "math": "Математика 8",
    "physics": "Физика 8",
    "chemistry": "Хемија 8",
}

# Quality flag → manim flag + output subfolder name
QUALITY_MAP = {
    "--lq": ("-ql", "480p15"),
    "--mq": ("-qm", "720p30"),
    "--hq": ("-qh", "1080p60"),
}


def collect_renders(args_subject, args_unit, args_lesson):
    """
    Return a flat list of (subject_key, unit_int, lesson_int, file, scene, title)
    tuples matching the given filter args (may be "all").
    """
    results = []

    subjects = (
        list(LESSONS.keys())
        if args_subject == "all"
        else [args_subject]
    )

    for subj in subjects:
        if subj not in LESSONS:
            print(f"Unknown subject '{subj}'. Available: {', '.join(LESSONS.keys())}")
            sys.exit(1)

        units = (
            list(LESSONS[subj].keys())
            if args_unit == "all"
            else [int(args_unit)]
        )

        for unit in units:
            if unit not in LESSONS[subj]:
                print(f"Unit {unit} not found in {subj}.")
                sys.exit(1)

            lessons = (
                list(LESSONS[subj][unit].keys())
                if args_lesson == "all"
                else [int(args_lesson)]
            )

            for lesson in lessons:
                if lesson not in LESSONS[subj][unit]:
                    print(f"Lesson {lesson} not found in {subj}, unit {unit}.")
                    sys.exit(1)
                file, scene, title = LESSONS[subj][unit][lesson]
                results.append((subj, unit, lesson, file, scene, title))

    return results


def print_lesson_list():
    print()
    for subj, units in LESSONS.items():
        label = SUBJECT_LABELS.get(subj, subj)
        print(f"  {label}")
        for unit, lessons in units.items():
            print(f"    Единица {unit}")
            for lesson, (file, scene, title) in lessons.items():
                exists = "OK" if os.path.isfile(os.path.join(THIS_DIR, file)) else "MISSING"
                print(f"      {lesson}. {title}  [{exists}]  ({file})")
        print()


def render_one(subj, unit, lesson, file, scene, title, manim_flag, quality_folder, index, total):
    label = SUBJECT_LABELS.get(subj, subj)
    print(f"\n[{index}/{total}] Rendering: {label} > Единица {unit} > Лекција {lesson}: {title}")

    script_path = os.path.join(THIS_DIR, file)
    if not os.path.isfile(script_path):
        print(f"  ERROR: Script not found: {script_path}")
        return False

    cmd = [sys.executable, "-m", "manim", manim_flag, script_path, scene]
    result = subprocess.run(cmd, cwd=THIS_DIR)

    if result.returncode == 0:
        # Derive expected output path from manim conventions
        stem = os.path.splitext(file)[0]
        out = os.path.join(THIS_DIR, "media", "videos", stem, quality_folder, f"{scene}.mp4")
        print(f"  Done  →  {out}")
        return True
    else:
        print(f"  FAILED (exit code {result.returncode})")
        return False


def main():
    THIS_DIR_global = os.path.dirname(os.path.abspath(__file__))
    global THIS_DIR
    THIS_DIR = THIS_DIR_global

    raw_args = sys.argv[1:]

    # Extract quality flag
    quality_flag = "--lq"
    filtered = []
    for a in raw_args:
        if a in QUALITY_MAP:
            quality_flag = a
        else:
            filtered.append(a)

    manim_flag, quality_folder = QUALITY_MAP[quality_flag]

    # No args → print list
    if len(filtered) == 0:
        print_lesson_list()
        return

    # "all" → all subjects
    if filtered[0] == "all":
        renders = collect_renders("all", "all", "all")

    elif len(filtered) == 1:
        # python render.py physics  → all units, all lessons
        renders = collect_renders(filtered[0], "all", "all")

    elif len(filtered) == 2:
        # python render.py physics all  → all lessons in all units
        # OR: python render.py physics 1  → all lessons in unit 1
        subj = filtered[0]
        second = filtered[1]
        if second == "all":
            renders = collect_renders(subj, "all", "all")
        else:
            renders = collect_renders(subj, second, "all")

    elif len(filtered) == 3:
        # python render.py physics 1 1  OR  python render.py physics 1 all
        subj   = filtered[0]
        unit   = filtered[1]
        lesson = filtered[2]
        renders = collect_renders(subj, unit, lesson)

    else:
        print(__doc__)
        sys.exit(1)

    if not renders:
        print("No lessons matched the given arguments.")
        sys.exit(1)

    total   = len(renders)
    passed  = 0
    failed  = 0

    for i, (subj, unit, lesson, file, scene, title) in enumerate(renders, start=1):
        ok = render_one(subj, unit, lesson, file, scene, title,
                        manim_flag, quality_folder, i, total)
        if ok:
            passed += 1
        else:
            failed += 1

    print(f"\n{'='*50}")
    print(f"Done. {passed} rendered, {failed} failed.  (quality: {quality_flag})")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
