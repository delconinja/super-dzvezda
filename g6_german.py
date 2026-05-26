# -*- coding: utf-8 -*-
"""Grade 6 German — BRO 1:1: 3 теми / ~7 lessons + 3 tests."""

GERMAN = [

unit('de6-1', 'Meine ersten Kontakte — Мои први контакти', [
    lesson('de6-1-1', 'Hallo! Поздравување и претставување', '''## Hallo! Greetings & Introductions

### Поздрави
| German | MK |
|---|---|
| Hallo! | Здраво! |
| Guten Morgen! | Добро утро! |
| Guten Tag! | Добар ден! |
| Guten Abend! | Добра вечер! |
| Gute Nacht! | Добра ноќ! |
| Auf Wiedersehen! / Tschüss! | Довидување! / Чао! |

### Претставување
- *Wie heißt du?* — Како се викаш?
- *Ich heiße Marko.* — Се викам Марко.
- *Mein Name ist Marko.* — Моето име е Марко.
- *Wie alt bist du?* — Колку години имаш?
- *Ich bin 12 Jahre alt.* — Имам 12 години.
- *Woher kommst du?* — Од каде си?
- *Ich komme aus Mazedonien.* — Од Македонија сум.
- *Wo wohnst du?* — Каде живееш?
- *Ich wohne in Skopje.* — Живеам во Скопје.

### Алфабет / звуци
Германскиот има 4 специјални букви: **ä, ö, ü, ß** (есцет).
- ä се чита како „е“
- ö ~ „о со устата на и“
- ü ~ „и со устата на у“
- ß = двојно s (ss)

### Броеви 1-10
eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn''', [
        mc('eg6-1-1-1', 'Како се вели „Добар ден“ на германски?', ['Hallo', 'Guten Tag', 'Tschüss', 'Danke'], 'Guten Tag', 'Tag = ден.', 'Guten Tag = Добар ден.'),
        mc('eg6-1-1-2', '„Ich heiße Anna“ значи:', ['Здраво Ана', 'Се викам Ана', 'Колку години имаш', 'Од Германија сум'], 'Се викам Ана', 'heißen = се вика.', '„Ich heiße Anna“ = Се викам Ана.'),
        mc('eg6-1-1-3', 'Бројот 5 на германски е:', ['vier', 'fünf', 'sechs', 'sieben'], 'fünf', '5 = fünf.', 'Fünf = 5.'),
        tf('eg6-1-1-4', 'Германскиот има буквата „ß“ (есцет).', 'Точно', 'Двојно s.', 'Точно — ß е специјална буква, изговор како двојно s.'),
    ]),
    lesson('de6-1-2', 'Familie und Interessen — Семејство и интереси', '''## Семејство (Familie)

| German | MK |
|---|---|
| die Mutter / Mama | мајка |
| der Vater / Papa | татко |
| die Schwester | сестра |
| der Bruder | брат |
| die Großmutter / Oma | баба |
| der Großvater / Opa | дедо |
| der Onkel | вујко/стрико |
| die Tante | тетка/стрина |

### Членови (артикли)
Германскиот има 3 рода и членови:
- **der** = машки (der Vater, der Bruder)
- **die** = женски (die Mutter, die Schwester)
- **das** = среден (das Kind, das Haus)
- **die** = множина (die Eltern)

### Глаголот sein (да биде)
| Лице | Форма |
|---|---|
| ich | bin |
| du | bist |
| er/sie/es | ist |
| wir | sind |
| ihr | seid |
| sie/Sie | sind |

## Интереси (Interessen)

- *Was machst du gern?* — Што сакаш да правиш?
- *Ich spiele Fußball.* — Играм фудбал.
- *Ich höre Musik.* — Слушам музика.
- *Ich lese Bücher.* — Читам книги.
- *Ich tanze.* — Танцувам.
- *Ich male.* — Сликам.

### Хобија
- Fußball, Basketball, Schwimmen, Lesen, Musik, Tanzen, Malen, Computerspiele''', [
        mc('eg6-1-2-1', 'Mutter значи:', ['татко', 'мајка', 'сестра', 'брат'], 'мајка', 'die Mutter.', 'Mutter = мајка.'),
        mc('eg6-1-2-2', 'Кој член оди со „Vater“?', ['der', 'die', 'das', 'ein'], 'der', 'Машки род.', 'Der Vater — машки род.'),
        mc('eg6-1-2-3', '„Ich bin 12“ значи:', ['Сакам 12', 'Имам 12 години', 'Има 12 деца', 'Девет се 12'], 'Имам 12 години', 'Возраст.', '„Ich bin 12 Jahre alt“ — имам 12 години.'),
        mc('eg6-1-2-4', 'Како велиш „Слушам музика“?', ['Ich spiele Musik', 'Ich höre Musik', 'Ich sehe Musik', 'Ich lese Musik'], 'Ich höre Musik', 'hören = слуша.', 'hören = слуша.'),
    ]),
    lesson('de6-1-test', 'Test — Erste Kontakte', '## Тест: Erste Kontakte', [
        mc('tg6-1-1', '„Tschüss“ значи:', ['Здраво', 'Чао/Довидување', 'Извини', 'Благодарам'], 'Чао/Довидување', 'Информален поздрав.', 'Tschüss = чао (информално).'),
        mc('tg6-1-2', 'Член на „Schwester“ е:', ['der', 'die', 'das', 'ein'], 'die', 'Женски род.', 'Die Schwester — женски род.'),
        mc('tg6-1-3', '„drei“ е:', ['1', '2', '3', '4'], '3', 'Drei = 3.', 'Drei = 3.'),
        mc('tg6-1-4', 'Како велиш „Од Македонија сум“?', ['Ich heiße Mazedonien', 'Ich komme aus Mazedonien', 'Ich bin in Mazedonien', 'Mein Name ist Mazedonien'], 'Ich komme aus Mazedonien', 'kommen aus = доаѓа од.', 'Ich komme aus Mazedonien = доаѓам од Македонија.'),
    ], is_test=True),
]),

unit('de6-2', 'Meine Umgebung — Мојата околина', [
    lesson('de6-2-1', 'Schule, Fächer und Zeit — Училиште, предмети, време', '''## Училиште (die Schule)

### Места во училиште
- die Schule — училиште
- das Klassenzimmer — училница
- die Bibliothek — библиотека
- die Turnhalle — спортска сала
- der Schulhof — школски двор

### Школски прибор
- der Bleistift — молив
- der Kuli / Kugelschreiber — пенкало
- das Heft — тетратка
- das Buch — книга
- die Tasche — торба
- der Rucksack — ранец

### Предмети (Schulfächer)
- Mathematik — математика
- Deutsch — германски
- Englisch — англиски
- Geschichte — историја
- Geografie — географија
- Biologie — биологија
- Sport — спорт
- Kunst — уметност
- Musik — музика

### Дни на неделата
Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag

### Времето (Uhrzeit)
- *Wie spät ist es?* — Колку е часот?
- *Es ist acht Uhr.* — Часот е 8.
- *Es ist halb neun.* — Половина 9 (8:30).
- *Es ist Viertel vor zehn.* — 15 пред 10 (9:45).
- *Es ist Viertel nach drei.* — 15 по 3 (3:15).''', [
        mc('eg6-2-1-1', 'Како се вели „училиште“?', ['Buch', 'Schule', 'Tasche', 'Stadt'], 'Schule', 'die Schule.', 'Schule = училиште.'),
        mc('eg6-2-1-2', 'Кој ден е „Mittwoch“?', ['Понеделник', 'Вторник', 'Среда', 'Четврток'], 'Среда', 'Mitt = средина на неделата.', 'Mittwoch = среда.'),
        mc('eg6-2-1-3', 'Како велиш „имам математика“?', ['Ich habe Mathe', 'Ich heiße Mathe', 'Ich komme aus Mathe', 'Ich gehe Mathe'], 'Ich habe Mathe', 'haben = има.', 'Ich habe Mathe = имам математика.'),
        mc('eg6-2-1-4', '„halb neun“ значи:', ['9:30', '8:30', '9:00', '8:00'], '8:30', 'Половина до 9.', 'Halb neun = половина (на пат) до 9 = 8:30. Внимавај — не 9:30!'),
    ]),
    lesson('de6-2-test', 'Test — Schule', '## Тест: Schule und Zeit', [
        mc('tg6-2-1', 'Sonntag е:', ['Сабота', 'Недела', 'Понеделник', 'Петок'], 'Недела', 'Sonn = Сонце.', 'Sonntag = недела (ден на сонцето).'),
        mc('tg6-2-2', '„Was machst du gern?“ значи:', ['Како се викаш?', 'Што сакаш да правиш?', 'Каде живееш?', 'Колку години имаш?'], 'Што сакаш да правиш?', 'machen = прави, gern = со задоволство.', 'Што сакаш да правиш во слободно време?'),
        mc('tg6-2-3', 'Бројот 7 на германски:', ['sechs', 'sieben', 'acht', 'neun'], 'sieben', '7 = sieben.', 'Sieben = 7.'),
        tf('tg6-2-4', '„Es ist drei Uhr“ значи „Часот е 3“.', 'Точно', 'Uhr = час.', 'Точно — Es ist drei Uhr = часот е 3.'),
    ], is_test=True),
]),

unit('de6-3', 'Meine Freizeit — Моето слободно време', [
    lesson('de6-3-1', 'Hobbys und Sport — Хобија и спорт', '''## Хобија (Hobbys)

- Lesen (читање)
- Schwimmen (пливање)
- Tanzen (танцување)
- Malen (сликање)
- Singen (пеење)
- Kochen (готвење)
- Reisen (патување)
- Computerspiele spielen (играње компјутерски игри)

## Спорт (Sport)

- Fußball spielen — игра фудбал
- Basketball spielen — игра кошарка
- Tennis spielen — игра тенис
- schwimmen — плива
- Rad fahren — вози велосипед
- Ski fahren — скија

### Глаголот mögen (сака)
| Лице | Форма |
|---|---|
| ich | mag |
| du | magst |
| er/sie/es | mag |
| wir | mögen |
| ihr | mögt |
| sie/Sie | mögen |

### Изразување интерес
- *Ich mag Fußball.* — Сакам фудбал.
- *Ich spiele gern Fußball.* — Со задоволство играм фудбал.
- *Mein Hobby ist Lesen.* — Мое хоби е читање.
- *Mein Lieblingssport ist Schwimmen.* — Омилен спорт ми е пливање.

### Прашања
- *Was ist dein Hobby?* — Кое е твое хоби?
- *Welchen Sport magst du?* — Кој спорт го сакаш?''', [
        mc('eg6-3-1-1', 'Како велиш „Сакам фудбал“?', ['Ich spiele Fußball', 'Ich mag Fußball', 'Ich heiße Fußball', 'Ich bin Fußball'], 'Ich mag Fußball', 'mögen = сака.', 'Ich mag = сакам.'),
        mc('eg6-3-1-2', '„schwimmen“ е:', ['танцување', 'пеење', 'пливање', 'трчање'], 'пливање', 'Schwimm = плива.', 'Schwimmen = пливање.'),
        mc('eg6-3-1-3', '„Mein Hobby ist Lesen“ значи:', ['Сакам да читам', 'Мое хоби е читање', 'Не сакам да читам', 'Колку години имам'], 'Мое хоби е читање', 'Hobby + Lesen.', '„Мое хоби е читање.“'),
        tf('eg6-3-1-4', '„gern“ значи „со задоволство“.', 'Точно', 'Додаток на глагол.', 'Точно — gern = со задоволство (рад). „Ich lese gern“ = со задоволство читам.'),
    ]),
    lesson('de6-3-test', 'Test — Hobbys', '## Тест: Hobbys und Sport', [
        mc('tg6-3-1', '„Tanzen“ е:', ['пеење', 'танцување', 'готвење', 'патување'], 'танцување', 'Tanz = танц.', 'Tanzen = танцување.'),
        mc('tg6-3-2', 'Како велиш „Возам велосипед“?', ['Ich gehe Rad', 'Ich fahre Rad', 'Ich spiele Rad', 'Ich höre Rad'], 'Ich fahre Rad', 'fahren = возење.', 'Rad fahren = возење велосипед.'),
        mc('tg6-3-3', '„Was ist dein Hobby?“ значи:', ['Како се викаш?', 'Кое е твое хоби?', 'Каде живееш?', 'Што јадеш?'], 'Кое е твое хоби?', 'dein = твоe.', 'Was ist dein Hobby = кое е твое хоби.'),
        mc('tg6-3-4', 'Ich _____ Tennis.', ['mag', 'magst', 'mögen', 'mögt'], 'mag', 'ich + mag.', 'Ich mag = сакам.'),
    ], is_test=True),
]),

]
