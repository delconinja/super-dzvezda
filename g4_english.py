# -*- coding: utf-8 -*-
"""Grade 4 English — BRO 1:1: 4 теми / 10 lessons + 4 tests."""

ENGLISH = [

unit('en4-1', 'My Small World: Family, Home & Friends', [
    lesson('en4-1-1', 'Family & Greetings', '''## Greetings

| English | MK |
|---|---|
| Hello! / Hi! | Здраво! |
| Good morning! | Добро утро! |
| Good afternoon! | Добар ден! |
| Good evening! | Добра вечер! |
| Goodbye! / Bye! | Довидување! |
| How are you? | Како си? |
| I`m fine, thanks. | Добро сум, благодарам. |
| Nice to meet you! | Мило ми е! |

## Introducing yourself

- *My name is **Marko**.*
- *I`m **8 years old**.*
- *I`m from **Macedonia**.*
- *I live in **Skopje**.*

## Family Members

| English | MK |
|---|---|
| father / dad | татко |
| mother / mum | мајка |
| brother | брат |
| sister | сестра |
| grandfather / grandpa | дедо |
| grandmother / grandma | баба |
| cousin | братучед |
| friend | пријател |

### Numbers 1-10
one, two, three, four, five, six, seven, eight, nine, ten

### Colors
red, blue, green, yellow, black, white, pink, brown, orange, purple''', [
        mc('e4e-1-1-1', 'Како се вели „Добро утро“?', ['Good night', 'Good morning', 'Hello', 'Bye'], 'Good morning', 'Morning = утро.', 'Good morning.'),
        mc('e4e-1-1-2', '„My mother“ значи:', ['татко', 'мајка', 'брат', 'сестра'], 'мајка', 'Mother.', 'Mother = мајка.'),
        mc('e4e-1-1-3', 'Бројот „seven“ е:', ['5', '6', '7', '8'], '7', 'Seven = 7.', 'Seven = 7.'),
        mc('e4e-1-1-4', 'Бојата „red“ е:', ['сино', 'црвено', 'зелено', 'жолто'], 'црвено', 'Red.', 'Red = црвено.'),
    ]),

    lesson('en4-1-2', 'House & Things', '''## My Home

### Rooms
| English | MK |
|---|---|
| bedroom | спална |
| living room | дневна |
| kitchen | кујна |
| bathroom | бања |
| dining room | трпезарија |
| garden | двор |

### Furniture
| English | MK |
|---|---|
| bed | кревет |
| table | маса |
| chair | стол |
| sofa | кауч |
| TV | телевизор |
| window | прозорец |
| door | врата |

## TO BE (am/is/are)

| Subject | Form |
|---|---|
| I | am |
| You / We / They | are |
| He / She / It | is |

### Examples
- *I am Marko.* (Јас сум Марко.)
- *She is my sister.* (Таа е сестра ми.)
- *They are my friends.* (Тие се пријатели.)

## Numbers 11-20

eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty

(Числата 13-19 завршуваат на **-teen**)''', [
        mc('e4e-1-2-1', 'Каде спиеш?', ['kitchen', 'bedroom', 'garden', 'living room'], 'bedroom', 'Bed = кревет.', 'Bedroom — соба со кревет.'),
        mc('e4e-1-2-2', 'Choose: She _____ my friend.', ['am', 'is', 'are', 'be'], 'is', 'She → is.', 'She/He/It → is.'),
        mc('e4e-1-2-3', '„Window“ е:', ['врата', 'прозорец', 'стол', 'маса'], 'прозорец', 'Window.', 'Window = прозорец.'),
        mc('e4e-1-2-4', 'Бројот 13 на англиски:', ['three', 'thirty', 'thirteen', 'third'], 'thirteen', '-teen.', 'Thirteen = 13.'),
    ]),

    lesson('en4-1-test', 'Test — Family & Home', '## Test: Family & Home', [
        mc('t4e-1-1', '„Good night“ значи:', ['Добро утро', 'Добар ден', 'Добра ноќ', 'Здраво'], 'Добра ноќ', 'Night = ноќ.', 'Good night.'),
        mc('t4e-1-2', 'Father значи:', ['мајка', 'татко', 'брат', 'сестра'], 'татко', 'Father.', 'Father = татко.'),
        mc('t4e-1-3', 'Choose: They _____ my friends.', ['am', 'is', 'are', 'be'], 'are', 'They → are.', 'They are.'),
        mc('t4e-1-4', 'Бројот „ten“:', ['1', '5', '10', '100'], '10', 'Ten = 10.', '10.'),
        mc('t4e-1-5', 'Бојата „blue“ е:', ['сино', 'црвено', 'жолто', 'зелено'], 'сино', 'Blue.', 'Blue = сино.'),
    ], is_test=True),
]),

unit('en4-2', 'My Outer World: School, Hobbies & Activities', [
    lesson('en4-2-1', 'School & Subjects', '''## School

### Vocabulary
| English | MK |
|---|---|
| school | училиште |
| classroom | училница |
| teacher | наставник |
| student / pupil | ученик |
| desk | клупа |
| bag / backpack | торба / ранец |
| book | книга |
| notebook | тетратка |
| pen | пенкало |
| pencil | молив |
| eraser | гумичка |
| ruler | линијар |

### Subjects
| English | MK |
|---|---|
| Maths | Математика |
| Macedonian | Македонски |
| English | Англиски |
| Science | Природни науки |
| History | Историја |
| Art | Ликовно |
| Music | Музичко |
| PE (Physical Education) | Физичко |

### Days of the week
**Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday**

### Sentences
- *I have Maths today.* (Денеска имам математика.)
- *I like Music.* (Сакам музичко.)
- *My favourite subject is English.*''', [
        mc('e4e-2-1-1', '„Teacher“ е:', ['наставник', 'ученик', 'татко', 'другар'], 'наставник', 'Teach.', 'Teacher = наставник.'),
        mc('e4e-2-1-2', 'Кој ден е „Friday“?', ['понеделник', 'четврток', 'петок', 'недела'], 'петок', 'Friday.', 'Friday = петок.'),
        mc('e4e-2-1-3', '„Notebook“ е:', ['книга', 'тетратка', 'торба', 'молив'], 'тетратка', 'Notebook.', 'Notebook = тетратка.'),
        tf('e4e-2-1-4', '„PE“ значи Physical Education = физичко образование.', 'True', 'PE = физичко.', 'True — PE = Physical Education.', mk=False),
    ]),

    lesson('en4-2-2', 'Hobbies & Likes', '''## Hobbies

| English | MK |
|---|---|
| football | фудбал |
| basketball | кошарка |
| tennis | тенис |
| swimming | пливање |
| reading | читање |
| drawing | цртање |
| singing | пеење |
| dancing | танцување |
| playing video games | играње игри |
| cooking | готвење |

## „I like / I don`t like“

- *I like football.* (Сакам фудбал.)
- *I don`t like vegetables.* (Не сакам зеленчук.)
- *I love reading.* (Обожавам да читам.)
- *I hate cleaning.* (Мразам чистење.)

## Present Simple

For routines:

| Subject | Verb |
|---|---|
| I / You / We / They | go, play, eat |
| He / She / It | go**es**, play**s**, eat**s** |

### Examples
- *I play football on Saturdays.*
- *She likes ice cream.*
- *They go to school.*

### Negative
- *I **don`t** like spinach.*
- *He **doesn`t** play basketball.*

### Question
- ***Do*** *you like pizza?* — Yes, I do.
- ***Does*** *she swim?* — No, she doesn`t.''', [
        mc('e4e-2-2-1', '„I like ____“ за хоби:', ['kitchen', 'football', 'house', 'sad'], 'football', 'Спорт.', 'I like football (хоби).'),
        mc('e4e-2-2-2', 'Choose: He _____ tennis.', ['play', 'plays', 'playing', 'is play'], 'plays', '3rd singular + s.', 'He/She/It → plays.'),
        mc('e4e-2-2-3', 'Negative: I _____ cabbage.', ['no like', 'don`t like', 'doesn`t like', 'not like'], 'don`t like', 'I → don`t.', 'I don`t like.'),
        tf('e4e-2-2-4', '„Reading“ значи читање.', 'Точно', 'Read = чита.', 'Точно — Reading = читање.'),
    ]),

    lesson('en4-2-test', 'Test — School & Hobbies', '## Test: School & Hobbies', [
        mc('t4e-2-1', '„Pencil“ е:', ['пенкало', 'молив', 'книга', 'тетратка'], 'молив', 'Pencil.', 'Pencil = молив.'),
        mc('t4e-2-2', 'Choose: She _____ to school.', ['go', 'goes', 'going', 'gone'], 'goes', '3rd singular.', 'She goes.'),
        mc('t4e-2-3', '„Saturday“ е:', ['понеделник', 'четврток', 'сабота', 'недела'], 'сабота', 'Saturday.', 'Saturday = сабота.'),
        mc('t4e-2-4', '„I love drawing“ значи:', ['Сакам да цртам', 'Сакам да пеам', 'Сакам да играм', 'Сакам да јадам'], 'Сакам да цртам', 'Drawing = цртање.', 'Сакам да цртам.'),
    ], is_test=True),
]),

unit('en4-3', 'Our Town and World: Places, Countries and Routines', [
    lesson('en4-3-1', 'Places & Directions', '''## Places in Town

| English | MK |
|---|---|
| park | парк |
| shop / store | продавница |
| hospital | болница |
| school | училиште |
| cinema | кино |
| restaurant | ресторан |
| post office | пошта |
| zoo | зоолошка градина |
| church | црква |
| library | библиотека |

### „Where is...?“
- *Where is the school?* — Каде е училиштето?
- *It`s on the corner.* — Тоа е на ќош.
- *It`s near the park.* — Близу до паркот.

### Prepositions
- **in** — во (in the box)
- **on** — на (on the table)
- **under** — под (under the chair)
- **next to** — до (next to the school)
- **near** — близу (near the park)

### Directions
- **left** — лево
- **right** — десно
- **straight on** — право

### Countries
| English | MK |
|---|---|
| Macedonia | Македонија |
| Greece | Грција |
| Bulgaria | Бугарија |
| Italy | Италија |
| Germany | Германија |
| France | Франција |
| England | Англија |
| Spain | Шпанија |
| USA | САД |''', [
        mc('e4e-3-1-1', '„Cinema“ е:', ['училиште', 'кино', 'пошта', 'болница'], 'кино', 'Films.', 'Cinema = кино.'),
        mc('e4e-3-1-2', '„On the table“ значи:', ['под маса', 'до маса', 'на маса', 'зад маса'], 'на маса', 'On.', 'On = на.'),
        mc('e4e-3-1-3', '„Turn left“ значи:', ['сврти десно', 'сврти лево', 'оди право', 'стоп'], 'сврти лево', 'Left.', 'Turn left.'),
        mc('e4e-3-1-4', '„Germany“ е:', ['Македонија', 'Грција', 'Германија', 'Италија'], 'Германија', 'Germany.', 'Germany = Германија.'),
    ]),

    lesson('en4-3-2', 'Daily Routines & Time', '''## Daily Routines

| English | MK |
|---|---|
| wake up | будам се |
| get up | станувам |
| have breakfast | појадувам |
| go to school | одам на училиште |
| have lunch | ручам |
| do homework | правам домашна |
| have dinner | вечерам |
| go to bed | одам на спиење |

### Sentences
- *I **wake up** at 7 o`clock.*
- *I **have breakfast** at 7:30.*
- *I **go to school** at 8.*
- *I **go to bed** at 10 PM.*

## Telling Time

- *What time is it?* — Колку е часот?
- *It`s 8 o`clock.* — 8:00
- *It`s half past 8.* — 8:30 (половина по 8)
- *It`s a quarter past 8.* — 8:15
- *It`s a quarter to 9.* — 8:45

### Useful phrases
- *in the morning* — наутро
- *in the afternoon* — попладне
- *in the evening* — навечер
- *at night* — ноќе

### Adverbs of frequency
**always** > **usually** > **often** > **sometimes** > **never**

- *I **always** wake up early.*
- *She **never** drinks coffee.*''', [
        mc('e4e-3-2-1', '„Wake up“ значи:', ['Спие', 'Буди се', 'Ручa', 'Игра'], 'Буди се', 'Wake up.', 'Wake up = буди се.'),
        mc('e4e-3-2-2', '„It`s half past 8“ значи:', ['8:00', '8:30', '8:15', '8:45'], '8:30', 'Half = половина.', '8:30.'),
        mc('e4e-3-2-3', '„In the morning“ е:', ['Наутро', 'Попладне', 'Навечер', 'Ноќе'], 'Наутро', 'Morning.', 'Наутро.'),
        mc('e4e-3-2-4', '„Always“ значи:', ['Никогаш', 'Понекогаш', 'Винаги', 'Често'], 'Винаги', '100%.', 'Always = винаги.'),
    ]),

    lesson('en4-3-test', 'Test — Places & Time', '## Test: Our Town & Routines', [
        mc('t4e-3-1', '„Park“ е:', ['училиште', 'парк', 'пошта', 'црква'], 'парк', 'Park.', 'Park = парк.'),
        mc('t4e-3-2', '„Get up“ значи:', ['Спие', 'Станува', 'Ручa', 'Игра'], 'Станува', 'Get up.', 'Get up = станува.'),
        mc('t4e-3-3', '„Italy“ е:', ['Италија', 'Грција', 'Германија', 'Шпанија'], 'Италија', 'Italy.', 'Italy = Италија.'),
        tf('t4e-3-4', '„Never“ значи никогаш.', 'Точно', '0%.', 'Точно — never = никогаш.'),
    ], is_test=True),
]),

unit('en4-4', 'Our Planet: Health, Nature and the Future', [
    lesson('en4-4-1', 'Health & Food', '''## Health

### Body parts
| English | MK |
|---|---|
| head | глава |
| eye | око |
| nose | нос |
| mouth | уста |
| ear | уво |
| hand | рака |
| leg | нога |
| foot | стапало |
| hair | коса |
| teeth | заби |

### Healthy / Unhealthy
- **Healthy**: овошје, зеленчук, вода, спорт
- **Unhealthy**: премногу слатки, фаст фуд, сода

### Sentences
- *I have a headache.* — Имам главоболка.
- *I feel sick.* — Се чувствувам болно.
- *Drink water!* — Пиј вода!

## Food

| English | MK |
|---|---|
| apple | јаболко |
| banana | банана |
| bread | леб |
| milk | млеко |
| cheese | сирење |
| fish | риба |
| meat | месо |
| vegetables | зеленчук |
| fruit | овошје |
| water | вода |

### „I eat / I drink“
- *I **eat** an apple every day.*
- *I **drink** water.*
- *Cats **eat** fish.*''', [
        mc('e4e-4-1-1', '„Apple“ е:', ['банана', 'јаболко', 'круша', 'портокал'], 'јаболко', 'Apple.', 'Apple = јаболко.'),
        mc('e4e-4-1-2', 'Тело: „eye“ е:', ['уво', 'око', 'нос', 'уста'], 'око', 'Eye.', 'Eye = око.'),
        mc('e4e-4-1-3', 'Healthy food:', ['candy', 'fast food', 'vegetables', 'soda'], 'vegetables', 'Здраво.', 'Vegetables — healthy.'),
        tf('e4e-4-1-4', 'Treba да пиеме многу вода.', 'Точно', 'Здравје.', 'Точно — drink water.'),
    ]),

    lesson('en4-4-2', 'Nature & Weather', '''## Animals

| English | MK |
|---|---|
| dog | куче |
| cat | мачка |
| bird | птица |
| fish | риба |
| horse | коњ |
| cow | крава |
| sheep | овца |
| pig | свиња |
| rabbit | заjак |
| lion | лав |
| elephant | слон |
| monkey | мајмун |

### Plants
| English | MK |
|---|---|
| tree | дрво |
| flower | цвет |
| grass | трева |
| leaf | лист |

## Weather

| English | MK |
|---|---|
| sunny | сончев |
| rainy | дождлив |
| cloudy | облачен |
| snowy | снежен |
| windy | ветровит |
| hot | топло |
| cold | студено |
| warm | топло (умерено) |

### „What`s the weather like?“
- *It`s sunny today.* (Денеска е сончево.)
- *It`s raining.* (Врне.)
- *It`s cold in winter.* (Зимата е студено.)

## Save the Planet

- **Recycle** — рециклирај
- **Reuse** — повторно користи
- **Reduce** — намали отпад
- **Plant trees** — сади дрвја
- **Save water** — заштеди вода
- **Save electricity** — заштеди струја''', [
        mc('e4e-4-2-1', '„Dog“ е:', ['куче', 'мачка', 'птица', 'риба'], 'куче', 'Dog.', 'Dog = куче.'),
        mc('e4e-4-2-2', '„Sunny“ значи:', ['дождлив', 'сончев', 'снежен', 'облачен'], 'сончев', 'Sun.', 'Sunny = сончев.'),
        mc('e4e-4-2-3', '„Recycle“ значи:', ['Hвргам', 'Рециклирам', 'Купувам', 'Гори'], 'Рециклирам', 'Re-cycle.', 'Recycle = рециклирам.'),
        tf('e4e-4-2-4', 'Треба да садиме дрвја за здрава планета.', 'Точно', 'Plant trees.', 'Точно.'),
    ]),

    lesson('en4-4-test', 'Test — Planet & Health', '## Test: Our Planet & Health', [
        mc('t4e-4-1', '„Healthy food“ е:', ['Candy', 'Vegetables', 'Soda', 'Fast food'], 'Vegetables', 'Здраво.', 'Vegetables.'),
        mc('t4e-4-2', '„Cat“ е:', ['куче', 'мачка', 'птица', 'риба'], 'мачка', 'Cat.', 'Cat = мачка.'),
        mc('t4e-4-3', '„Rainy“ значи:', ['сончев', 'дождлив', 'снежен', 'облачен'], 'дождлив', 'Rain.', 'Rainy = дождлив.'),
        tf('t4e-4-4', 'Recycle помага на природата.', 'Точно', 'Помалку отпад.', 'Точно.'),
    ], is_test=True),
]),

]
