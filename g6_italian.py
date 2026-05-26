# -*- coding: utf-8 -*-
"""Grade 6 Italian — BRO 1:1: 3 теми / 7 lessons + 3 tests."""

ITALIAN = [

unit('it6-1', 'Primi contatti — Први контакти', [
    lesson('it6-1-1', 'Ciao! Поздравување и претставување', '''## Поздрави

| Italian | MK |
|---|---|
| Ciao! | Здраво/Чао! |
| Buongiorno! | Добар ден! |
| Buonasera! | Добра вечер! |
| Buonanotte! | Добра ноќ! |
| Arrivederci! | Довидување! |
| Grazie! | Благодарам! |
| Per favore | Ве молам |
| Scusa / Scusi | Извини/те |

## Претставување

- *Come ti chiami?* — Како се викаш?
- *Mi chiamo Marco.* — Се викам Марко.
- *Quanti anni hai?* — Колку години имаш?
- *Ho dodici anni.* — Имам 12 години.
- *Di dove sei?* — Од каде си?
- *Sono di Macedonia.* / *Vengo dalla Macedonia.* — Од Македонија сум.
- *Dove abiti?* — Каде живееш?
- *Abito a Skopje.* — Живеам во Скопје.

## Алфабет и фонетика

Италијанскиот користи 21 буква (без j, k, w, x, y во домашни зборови).

### Особени звуци
- **c** + a/o/u = „к“ (casa = каса)
- **c** + e/i = „ч“ (cena = чена)
- **ch** = „к“ (chiesa = киеза)
- **g** + a/o/u = „г“ (gatto = гато)
- **g** + e/i = „џ“ (gente = ѓенте)
- Сите букви се читаат — нема немо!

### Броеви 1-10
uno, due, tre, quattro, cinque, sei, sette, otto, nove, dieci''', [
        mc('ei6-1-1-1', 'Како се вели „Добар ден“?', ['Ciao', 'Buongiorno', 'Buonanotte', 'Grazie'], 'Buongiorno', 'Buon + giorno.', 'Buongiorno = добар ден.'),
        mc('ei6-1-1-2', '„Mi chiamo Anna“ значи:', ['Здраво Ана', 'Се викам Ана', 'Од Ана сум', 'Имам Ана'], 'Се викам Ана', 'chiamarsi = се вика.', 'Mi chiamo = се викам.'),
        mc('ei6-1-1-3', 'Бројот 5 на италијански:', ['quattro', 'cinque', 'sei', 'sette'], 'cinque', '5 = cinque.', 'Cinque = 5.'),
        tf('ei6-1-1-4', 'Италијанскиот ги чита сите букви во зборот.', 'Точно', 'Нема немо.', 'Точно — за разлика од францускиот, италијанскиот ги чита сите букви.'),
    ]),
    lesson('it6-1-2', 'Famiglia e interessi — Семејство и интереси', '''## Семејство (la famiglia)

| Italian | MK |
|---|---|
| la madre / mamma | мајка |
| il padre / papà | татко |
| la sorella | сестра |
| il fratello | брат |
| la nonna | баба |
| il nonno | дедо |
| lo zio | вујко/стрико |
| la zia | тетка/стрина |
| il cugino / la cugina | братучед/братучетка |

### Членови (артикли)
- **il** — машки определен (il padre)
- **la** — женски определен (la madre)
- **lo** — машки пред s+согл, z (lo zio, lo studente)
- **i** — машки множина (i padri)
- **le** — женски множина (le madri)
- **un** — машки неопределен (un libro)
- **una** — женски неопределен (una casa)

### Глаголот essere (да биде)
| Лице | Форма |
|---|---|
| io | sono |
| tu | sei |
| lui/lei | è |
| noi | siamo |
| voi | siete |
| loro | sono |

## Интереси

- *Cosa ti piace fare?* — Што сакаш да правиш?
- *Mi piace leggere.* — Сакам да читам.
- *Mi piace giocare a calcio.* — Сакам да играм фудбал.
- *Mi piacciono i film.* — Сакам филмови.

### Хобија
lo sport, la musica, la lettura, il cinema, i videogiochi, la danza''', [
        mc('ei6-1-2-1', '„madre“ значи:', ['татко', 'мајка', 'сестра', 'брат'], 'мајка', 'la madre.', 'Madre = мајка.'),
        mc('ei6-1-2-2', 'Член на „zio“ е:', ['il', 'la', 'lo', 'le'], 'lo', 'Пред z = lo.', 'Lo zio — машки определен пред „z“.'),
        mc('ei6-1-2-3', '„Ho 12 anni“ значи:', ['Сакам 12', 'Имам 12 години', 'Тука сум 12', 'Постарам 12'], 'Имам 12 години', 'avere = има, anni = години.', 'Ho ... anni = имам ... години.'),
        mc('ei6-1-2-4', 'Како велиш „Сакам музика“?', ['Mi chiamo musica', 'Mi piace la musica', 'Sono musica', 'Ho musica'], 'Mi piace la musica', 'mi piace = ми се допаѓа.', 'Mi piace = ми се допаѓа/сакам.'),
    ]),
    lesson('it6-1-test', 'Test — Primi contatti', '## Тест: Primi contatti', [
        mc('ti6-1-1', '„Arrivederci“ значи:', ['Здраво', 'Довидување', 'Благодарам', 'Извини'], 'Довидување', 'При разделба.', 'Arrivederci = довидување.'),
        mc('ti6-1-2', 'Член на „sorella“:', ['il', 'la', 'lo', 'i'], 'la', 'Женски.', 'La sorella — женски определен.'),
        mc('ti6-1-3', 'Бројот 7 на италијански:', ['sei', 'sette', 'otto', 'nove'], 'sette', '7 = sette.', 'Sette = 7.'),
        mc('ti6-1-4', 'Како велиш „Од Македонија сум“?', ['Mi chiamo Macedonia', 'Sono di Macedonia', 'Ho Macedonia', 'Piace Macedonia'], 'Sono di Macedonia', 'sono di = сум од.', 'Sono di Macedonia = од Македонија сум.'),
    ], is_test=True),
]),

unit('it6-2', 'La scuola — Училиштето', [
    lesson('it6-2-1', 'Materie, giorni e ora', '''## Училиште (la scuola)

### Школски прибор
- la penna — пенкало
- la matita — молив
- il quaderno — тетратка
- il libro — книга
- l`astuccio — пенал
- lo zaino — ранец

### Предмети (le materie)
- la matematica — математика
- l`italiano — италијански
- l`inglese — англиски
- la storia — историја
- la geografia — географија
- la biologia — биологија
- l`educazione fisica — спорт/физичко
- la musica — музика
- l`arte — уметност

### Дни на неделата
lunedì, martedì, mercoledì, giovedì, venerdì, sabato, domenica

### Времето (l`ora)
- *Che ora è?* / *Che ore sono?* — Колку е часот?
- *Sono le otto.* — Часот е 8.
- *Sono le otto e mezza.* — 8:30.
- *Sono le nove meno un quarto.* — 8:45.
- *Sono le nove e un quarto.* — 9:15.

### Часови
- *Ho italiano il lunedì.* — Имам италијански во понеделник.
- *La lezione comincia alle otto.* — Часот почнува во 8.''', [
        mc('ei6-2-1-1', '„libro“ значи:', ['пенал', 'тетратка', 'книга', 'молив'], 'книга', 'il libro.', 'Libro = книга.'),
        mc('ei6-2-1-2', '„mercoledì“ е:', ['Понеделник', 'Вторник', 'Среда', 'Четврток'], 'Среда', 'Среден ден.', 'Mercoledì = среда.'),
        mc('ei6-2-1-3', '„Sono le otto e mezza“ значи:', ['8:00', '8:30', '8:15', '8:45'], '8:30', 'mezza = половина.', 'E mezza = и половина → 8:30.'),
        mc('ei6-2-1-4', 'Како велиш „Имам математика“?', ['Sono matematica', 'Ho matematica', 'Piace matematica', 'Chiamo matematica'], 'Ho matematica', 'avere = има.', 'Ho matematica = имам математика.'),
    ]),
    lesson('it6-2-test', 'Test — La scuola', '## Тест: La scuola', [
        mc('ti6-2-1', '„domenica“ е:', ['Сабота', 'Недела', 'Понеделник', 'Петок'], 'Недела', 'Ден на Господа.', 'Domenica = недела.'),
        mc('ti6-2-2', '„Che ora è?“ значи:', ['Колку години?', 'Колку е часот?', 'Кој дел?', 'Каде си?'], 'Колку е часот?', 'ora = час.', 'Che ora è = колку е часот.'),
        mc('ti6-2-3', 'Бројот 9 на италијански:', ['otto', 'nove', 'dieci', 'sette'], 'nove', '9 = nove.', 'Nove = 9.'),
        tf('ti6-2-4', '„il sabato“ значи „во сабота“.', 'Точно', 'Со определен член = редовно.', 'Точно — il + ден значи „редовно во тој ден“.'),
    ], is_test=True),
]),

unit('it6-3', 'Il tempo libero — Слободно време', [
    lesson('it6-3-1', 'Le attività e i verbi irregolari', '''## Активности во слободно време

- giocare a calcio — игра фудбал
- giocare a pallacanestro — игра кошарка
- nuotare — плива
- ballare — танцува
- cantare — пее
- leggere — чита
- ascoltare la musica — слуша музика
- guardare la TV — гледа ТВ
- fare sport — спортува
- andare in bicicletta — вози велосипед

### Неправилен глагол andare (оди)
| Лице | Форма |
|---|---|
| io | vado |
| tu | vai |
| lui/lei | va |
| noi | andiamo |
| voi | andate |
| loro | vanno |

### Неправилен глагол fare (прави)
| Лице | Форма |
|---|---|
| io | faccio |
| tu | fai |
| lui/lei | fa |
| noi | facciamo |
| voi | fate |
| loro | fanno |

### „mi piace/mi piacciono“
- *Mi piace + единствена именка/глагол*: Mi piace la musica. Mi piace cantare.
- *Mi piacciono + множина именки*: Mi piacciono i film.

### Интензитет
- Mi piace molto... — многу ми се допаѓа
- Adoro... — обожавам
- Non mi piace... — не ми се допаѓа
- Odio... — мразам''', [
        mc('ei6-3-1-1', '„nuotare“ значи:', ['танцува', 'пее', 'плива', 'трча'], 'плива', 'Nuotare.', 'Nuotare = плива.'),
        mc('ei6-3-1-2', 'Како велиш „Сакам да читам“?', ['Mi chiamo leggere', 'Mi piace leggere', 'Sono leggere', 'Ho leggere'], 'Mi piace leggere', 'mi piace + infinitive.', 'Mi piace leggere = сакам да читам.'),
        mc('ei6-3-1-3', '„andare in bicicletta“ значи:', ['танцува', 'плива', 'вози велосипед', 'спортува'], 'вози велосипед', 'bicicletta = велосипед.', 'Andare in bicicletta = возење велосипед.'),
        mc('ei6-3-1-4', '„adoro lo sport“ е:', ['Не сакам спорт', 'Сакам спорт', 'Обожавам спорт', 'Мразам спорт'], 'Обожавам спорт', 'adorare = обожава.', 'Adoro = обожавам (поголем интензитет).'),
    ]),
    lesson('it6-3-test', 'Test — Tempo libero', '## Тест: Tempo libero', [
        mc('ti6-3-1', '„cantare“ значи:', ['танцува', 'пее', 'игра', 'спие'], 'пее', 'Cantare.', 'Cantare = пее.'),
        mc('ti6-3-2', '„Odio i compiti“ значи:', ['Сакам домашна', 'Мразам домашна', 'Имам домашна', 'Правам домашна'], 'Мразам домашна', 'odiare = мрази.', 'Odio = мразам.'),
        mc('ti6-3-3', 'Io _____ a scuola.', ['vado', 'vai', 'va', 'vanno'], 'vado', 'io + vado.', 'Io vado = јас одам.'),
        tf('ti6-3-4', 'Глаголот „fare“ е неправилен.', 'Точно', 'faccio, fai, fa...', 'Точно — fare е еден од најчестите неправилни глаголи.'),
    ], is_test=True),
]),

]
