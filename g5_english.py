# -*- coding: utf-8 -*-
"""Grade 5 English — BRO 1:1: 4 теми / 10 lessons + 4 tests."""

ENGLISH = [

unit('en5-1', 'My Little World: Family & Friends', [
    lesson('en5-1-1', 'Family Vocabulary & TO BE / HAVE GOT', '''## Family

| English | MK |
|---|---|
| father / dad | татко |
| mother / mum | мајка |
| brother | брат |
| sister | сестра |
| grandfather | дедо |
| grandmother | баба |
| uncle | вујко/стрико |
| aunt | тетка/стрина |
| cousin | братучед/братучетка |
| friend | пријател |

## TO BE (am / is / are)

| Subject | Form |
|---|---|
| I | **am** |
| You / We / They | **are** |
| He / She / It | **is** |

### Examples
- *I **am** Maja.*
- *He **is** my brother.*
- *They **are** my friends.*

### Negative
- *I **am not (I`m not)** tired.*
- *She **is not (isn`t)** here.*
- *They **are not (aren`t)** at school.*

### Questions
- ***Are*** *you OK?* — Yes, I am.
- ***Is*** *he your brother?* — Yes, he is.

## HAVE GOT

To express ownership/possession.

| Subject | Form |
|---|---|
| I / You / We / They | **have got** |
| He / She / It | **has got** |

### Examples
- *I **have got** a dog.*
- *She **has got** two sisters.*
- *We **have got** a big house.*

### Negative
- *I **haven`t got** a cat.*
- *He **hasn`t got** a bike.*

### Questions
- ***Have*** *you **got** a brother?* — Yes, I have.
- ***Has*** *she **got** a sister?* — No, she hasn`t.''', [
        mc('e5e-1-1-1', 'Choose: She _____ my sister.', ['am', 'is', 'are', 'be'], 'is', 'He/She/It → is.', '„She is“ — third person singular.'),
        mc('e5e-1-1-2', 'I _____ a dog.', ['has got', 'have got', 'is got', 'are got'], 'have got', 'I → have got.', 'I / You / We / They → have got.'),
        mc('e5e-1-1-3', 'My mother`s sister is my:', ['aunt', 'uncle', 'cousin', 'grandma'], 'aunt', 'Сестра на родител.', 'Aunt = тетка/стрина.'),
        mc('e5e-1-1-4', 'Negative of „He is happy“:', ['He no happy', 'He isn`t happy', 'He aren`t happy', 'He don`t happy'], 'He isn`t happy', 'is + not = isn`t.', 'He is not = isn`t.'),
    ]),

    lesson('en5-1-2', 'Adjectives & Comparatives', '''## Describing People

### Physical
- **tall / short** (висок / низок)
- **slim / thin / fat** (слаб / дебел)
- **young / old** (млад / стар)
- **long / short hair**
- **dark / blonde / red hair**
- **blue / brown / green eyes**

### Character
- **kind, friendly, polite**
- **smart, clever**
- **funny, serious**
- **lazy, hardworking**
- **shy, confident**

### Examples
- *My sister is tall and slim.*
- *He has dark hair and blue eyes.*
- *She is very kind.*

## Comparatives & Superlatives

### Short adjectives (+ er / est)
| Positive | Comparative | Superlative |
|---|---|---|
| tall | tall**er** | the tall**est** |
| big | big**ger** | the big**gest** |
| happy | happ**ier** | the happ**iest** |

(Rules: short adj + -er; double consonant after vowel+consonant; y → i)

### Long adjectives (more / the most)
| Positive | Comparative | Superlative |
|---|---|---|
| beautiful | **more** beautiful | **the most** beautiful |
| interesting | more interesting | the most interesting |

### Irregular
| Positive | Comparative | Superlative |
|---|---|---|
| good | **better** | **the best** |
| bad | **worse** | **the worst** |

### Examples
- *My brother is **taller** than me.*
- *Math is **more interesting** than history.*
- *She is **the best** singer in our class.*''', [
        mc('e5e-1-2-1', 'Comparative of „tall“:', ['taller', 'tallest', 'more tall', 'most tall'], 'taller', 'Short adj + -er.', 'Short adjectives add -er for comparative.'),
        mc('e5e-1-2-2', 'Superlative of „good“:', ['gooder', 'more good', 'the best', 'goodest'], 'the best', 'Irregular.', 'good → better → the best.'),
        mc('e5e-1-2-3', 'Comparative of „happy“:', ['happyer', 'happier', 'more happy', 'happiest'], 'happier', 'y → i + er.', 'Happy → happier.'),
        tf('e5e-1-2-4', 'Long adjectives use „more“ and „the most“.', 'True', '2+ syllables.', 'True — long adjectives use more/most.', mk=False),
    ]),

    lesson('en5-1-test', 'Test — Family & Friends', '## Test: Family & Friends', [
        mc('t5e-1-1', 'My father`s mother is my:', ['aunt', 'grandmother', 'cousin', 'sister'], 'grandmother', 'Mother of parent.', 'Grandmother = баба.'),
        mc('t5e-1-2', 'They _____ in Skopje.', ['is', 'am', 'are', 'be'], 'are', 'They → are.', 'They are.'),
        mc('t5e-1-3', 'She _____ a sister.', ['have got', 'has got', 'is got', 'be got'], 'has got', 'She → has got.', 'She/He/It → has got.'),
        mc('t5e-1-4', 'Comparative of „big“:', ['biger', 'bigger', 'biggest', 'more big'], 'bigger', 'Double consonant.', 'Big → bigger (double g).'),
        mc('t5e-1-5', 'Superlative of „bad“:', ['worse', 'the worst', 'badder', 'baddest'], 'the worst', 'Irregular.', 'bad → worse → the worst.'),
    ], is_test=True),
]),

unit('en5-2', 'My World Outside: School & Free Time', [
    lesson('en5-2-1', 'Time, Days & Present Simple', '''## Time

### Hours
- *What`s the time?* — Колку е часот?
- *It`s 8 o`clock.* — 8 часот
- *It`s half past 8.* — 8:30 (половина по)
- *It`s a quarter past 8.* — 8:15
- *It`s a quarter to 9.* — 8:45 (без четвртина до)

### Days of the week
- Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

### Months
- January, February, March, April, May, June, July, August, September, October, November, December

## Present Simple

For **routines** and **habits**.

| Subject | Verb |
|---|---|
| I / You / We / They | go, eat, play |
| He / She / It | go**es**, eat**s**, play**s** |

(Third person singular adds **-s** or **-es**.)

### Examples
- *I **go** to school every day.*
- *She **plays** football.*
- *They **eat** dinner at 7.*

### Negative (don`t / doesn`t)
- *I **don`t** like vegetables.*
- *He **doesn`t** play football.*

### Questions (do / does)
- ***Do*** *you play games?* — Yes, I do.
- ***Does*** *she like math?* — No, she doesn`t.

### Adverbs of frequency
**always** (100%) > **usually** > **often** > **sometimes** > **rarely** > **never** (0%)

Position: before the main verb.
- *She **always** wakes up early.*
- *I **never** drink coffee.*''', [
        mc('e5e-2-1-1', 'It`s 8:30. → It`s _____ past 8.', ['quarter', 'half', 'thirty', 'three'], 'half', '30 min = half.', 'Half past 8 = 8:30.'),
        mc('e5e-2-1-2', 'She _____ to school.', ['go', 'goes', 'going', 'gone'], 'goes', '3rd singular + s/es.', 'She goes (third person singular).'),
        mc('e5e-2-1-3', '_____ you like pizza?', ['Is', 'Are', 'Do', 'Does'], 'Do', 'You → do.', 'Do you...?'),
        mc('e5e-2-1-4', 'Adverb meaning „every time“:', ['never', 'sometimes', 'always', 'rarely'], 'always', '100%.', 'Always = 100% of the time.'),
    ]),

    lesson('en5-2-2', 'Present Continuous & Future Plans', '''## Present Continuous

For actions happening **right now**.

### Form
**Subject + am/is/are + verb-ing**

| Subject | Form |
|---|---|
| I | am playing |
| You / We / They | are playing |
| He / She / It | is playing |

### Examples
- *I am reading.*
- *She is talking on the phone.*
- *They are watching TV.*

### Negative
- *I am **not** working.*
- *She is**n`t** sleeping.*
- *They are**n`t** playing.*

### Question
- ***Are*** *you reading?*
- ***Is*** *he sleeping?*

### Spelling rules for -ing
- run → run**ning** (double consonant)
- write → writ**ing** (drop e)
- play → play**ing** (just add -ing)

## Present Simple vs Continuous

| Present Simple | Present Continuous |
|---|---|
| routines, habits | right now |
| every day, always | now, at the moment |
| *She works.* | *She is working.* |

## Future Plans — „going to“

For planned future actions:

**Subject + am/is/are + going to + verb**

- *I **am going to** visit my grandma tomorrow.*
- *They **are going to** play tennis next week.*
- *She **is going to** buy a new phone.*''', [
        mc('e5e-2-2-1', 'Choose: She _____ a book right now.', ['read', 'reads', 'is reading', 'readed'], 'is reading', 'Now = continuous.', 'Right now → Present Continuous.'),
        mc('e5e-2-2-2', 'I _____ visit Paris next summer.', ['am going to', 'will going', 'going', 'go'], 'am going to', 'Future plan.', '„Going to“ for plans.'),
        mc('e5e-2-2-3', 'Spelling of „run“ + ing:', ['runing', 'running', 'runs', 'runed'], 'running', 'Double consonant.', 'Run → running (double n).'),
        tf('e5e-2-2-4', 'Present Continuous is for routines.', 'False', 'Routines = Simple.', 'False — Present Simple for routines, Continuous for now.', mk=False),
    ]),

    lesson('en5-2-test', 'Test — School & Free Time', '## Test: My World Outside', [
        mc('t5e-2-1', 'It`s 8:15. → It`s a _____ past 8.', ['half', 'quarter', 'thirty', 'fifteen'], 'quarter', '15 min = quarter.', 'Quarter past = 15 min after.'),
        mc('t5e-2-2', 'She _____ tennis on Saturdays.', ['play', 'plays', 'playing', 'is playing'], 'plays', '3rd singular + s.', 'She plays (routine).'),
        mc('t5e-2-3', 'They _____ now.', ['eat', 'eats', 'are eating', 'is eating'], 'are eating', 'Now = continuous.', 'Right now → Continuous.'),
        mc('t5e-2-4', 'Adverb of frequency meaning „0%“:', ['always', 'sometimes', 'often', 'never'], 'never', '0% of time.', 'Never = 0%.'),
        mc('t5e-2-5', 'I _____ see my friend tomorrow.', ['am going to', 'will going', 'goes', 'is'], 'am going to', 'Future plan.', '„Going to“ for plans.'),
    ], is_test=True),
]),

unit('en5-3', 'Our Town, Our World', [
    lesson('en5-3-1', 'Places in Town & Directions', '''## Places in Town

| English | MK |
|---|---|
| school | училиште |
| hospital | болница |
| supermarket | маркет |
| restaurant | ресторан |
| bank | банка |
| post office | пошта |
| park | парк |
| library | библиотека |
| cinema | кино |
| church | црква |
| pharmacy | аптека |
| museum | музеј |
| bus station | автобуска станица |

## Asking for Directions

### Useful phrases
- *Excuse me, where is the post office?*
- *How can I get to the museum?*
- *Is it far from here?*

### Giving directions
- **Go straight on** — оди право
- **Turn left / right** — сврти лево/десно
- **Take the first / second turn**
- **Go past the supermarket** — помини покрај
- **It`s on the corner / on your left**
- **Next to / opposite / between**

### Prepositions of place
- **on** — на
- **in** — во
- **under** — под
- **next to** — до
- **in front of** — пред
- **behind** — зад
- **between** — помеѓу
- **opposite** — наспроти

### Examples
- *The cat is **on** the table.*
- *The book is **in** the bag.*
- *The school is **next to** the park.*''', [
        mc('e5e-3-1-1', 'Where do you borrow books?', ['restaurant', 'library', 'bank', 'park'], 'library', 'Books → library.', 'Library — место за позајмување книги.'),
        mc('e5e-3-1-2', '„Turn right“ значи:', ['Оди право', 'Сврти десно', 'Сврти лево', 'Стани'], 'Сврти десно', 'Right = десно.', 'Turn right = сврти десно.'),
        mc('e5e-3-1-3', 'The cat is _____ the box (under it).', ['on', 'in', 'under', 'next to'], 'under', 'Под.', 'Under = под.'),
        mc('e5e-3-1-4', '„Opposite“ значи:', ['до', 'наспроти', 'на', 'во'], 'наспроти', 'Спротивна страна.', 'Opposite = наспроти.'),
    ]),

    lesson('en5-3-2', 'Professions & Past Simple of TO BE', '''## Professions

| English | MK |
|---|---|
| teacher | наставник |
| doctor | лекар |
| nurse | медицинска сестра |
| police officer | полицаец |
| firefighter | пожарникар |
| chef / cook | готвач |
| baker | пекар |
| farmer | земјоделец |
| driver | возач |
| pilot | пилот |
| engineer | инженер |
| artist | уметник |
| actor / actress | актер / актерка |
| singer | пејач |
| writer | писател |

### What do they do?
- *A teacher **teaches** students.*
- *A doctor **helps** sick people.*
- *A baker **makes** bread.*
- *A farmer **grows** food.*

## Past Simple of TO BE

| Subject | Past |
|---|---|
| I / He / She / It | **was** |
| You / We / They | **were** |

### Examples
- *I **was** at school yesterday.*
- *She **was** sick last week.*
- *They **were** at the cinema.*

### Negative
- *I **was not (wasn`t)** tired.*
- *They **were not (weren`t)** there.*

### Questions
- ***Was*** *he at home?* — Yes, he was.
- ***Were*** *they at the party?* — No, they weren`t.

### Time expressions for past
- yesterday — вчера
- last week / month / year
- two days ago
- in 2020''', [
        mc('e5e-3-2-1', 'Who helps sick people?', ['teacher', 'doctor', 'baker', 'farmer'], 'doctor', 'Heal people.', 'Doctor = лекар.'),
        mc('e5e-3-2-2', 'Past Simple: I _____ at school yesterday.', ['am', 'is', 'was', 'were'], 'was', 'I → was.', 'I was (past of am).'),
        mc('e5e-3-2-3', 'They _____ in the park last weekend.', ['was', 'were', 'are', 'is'], 'were', 'They → were.', 'They were.'),
        tf('e5e-3-2-4', '„Yesterday“ means „in the past“.', 'True', 'One day ago.', 'True — yesterday is past.', mk=False),
    ]),

    lesson('en5-3-test', 'Test — Our Town', '## Test: Our Town, Our World', [
        mc('t5e-3-1', 'Where do you watch a film?', ['library', 'hospital', 'cinema', 'park'], 'cinema', 'Films.', 'Cinema — кино.'),
        mc('t5e-3-2', 'A _____ teaches students.', ['doctor', 'teacher', 'baker', 'pilot'], 'teacher', 'School.', 'Teacher — наставник.'),
        mc('t5e-3-3', 'I _____ tired yesterday.', ['am', 'is', 'was', 'were'], 'was', 'I → was.', 'I was tired yesterday.'),
        mc('t5e-3-4', '„Turn left“ значи:', ['Сврти десно', 'Сврти лево', 'Оди право', 'Стани'], 'Сврти лево', 'Left = лево.', 'Turn left = сврти лево.'),
    ], is_test=True),
]),

unit('en5-4', 'Our Planet, Our Health & Future', [
    lesson('en5-4-1', 'Health, Food & Modal Verb CAN', '''## Health & Food

### Healthy / Unhealthy
- **Healthy**: fruits, vegetables, water, exercise
- **Unhealthy**: too much sugar, fast food, soda

### Food vocabulary
- fruits: apple, banana, orange, grape, strawberry
- vegetables: carrot, potato, tomato, broccoli, lettuce
- protein: chicken, fish, eggs, beans
- dairy: milk, cheese, yoghurt
- grains: bread, rice, pasta

### Health phrases
- *I feel sick.*
- *I have a headache / stomachache / toothache.*
- *Take this medicine.*
- *Go to the doctor.*

## Modal Verb CAN

To express **ability** or **permission**.

### Form
**Subject + can + base verb**

### Examples
- *I **can** swim.* (ability)
- *She **can** speak three languages.*
- *We **can** go now.* (permission)

### Negative: can`t (cannot)
- *He **can`t** drive yet (he`s only 12).*
- *I **can`t** see well without my glasses.*

### Question
- ***Can*** *you swim?* — Yes, I can.
- ***Can*** *she play piano?* — No, she can`t.

### Polite requests
- ***Can*** *you help me?* (Можеш ли да ми помогнеш?)
- ***Can*** *I borrow your pen?*''', [
        mc('e5e-4-1-1', 'Which is healthy food?', ['Soda', 'Fast food', 'Vegetables', 'Candy'], 'Vegetables', 'Healthy.', 'Vegetables are healthy.'),
        mc('e5e-4-1-2', 'I _____ swim very well.', ['am', 'do', 'can', 'is'], 'can', 'Ability.', '„Can“ for ability.'),
        mc('e5e-4-1-3', 'Negative of „I can sing“:', ['I no can sing', 'I don`t can sing', 'I can`t sing', 'I am not sing'], 'I can`t sing', 'can + not = can`t.', 'Can not = can`t.'),
        tf('e5e-4-1-4', '„Can“ can express permission.', 'True', 'Can I...?', 'True — „Can I...“ asks for permission.', mk=False),
    ]),

    lesson('en5-4-2', 'Weather, Ecology & Our Planet', '''## Weather

### Conditions
- **sunny** — сончев
- **cloudy** — облачен
- **rainy** — дождлив
- **snowy** — снежен
- **windy** — ветровит
- **foggy** — магловит
- **stormy** — бурен

### Temperature
- *It`s hot / warm / cool / cold / freezing.*
- *The temperature is 20°C.*

### Useful sentences
- *What`s the weather like?*
- *How`s the weather?*
- *It`s raining.* (Continuous)
- *It often rains in November.* (Simple)

## Ecology & Our Planet

### Problems
- **Pollution** — air, water, soil
- **Climate change** — global warming
- **Deforestation** — cutting forests
- **Litter / rubbish** — too much garbage
- **Endangered species** — animals at risk

### What can WE do?
- **Recycle** paper, plastic, glass
- **Reuse** bags, bottles
- **Reduce** electricity and water
- **Walk or cycle** instead of car
- **Plant trees**
- **Don`t litter**

### „We must / should...“
- *We **must** protect the environment.*
- *We **should** recycle more.*
- *We **shouldn`t** waste water.*

## Future of Our Planet

- Switching to **clean energy** (solar, wind)
- Electric cars
- Less plastic
- More green spaces
- Education and awareness''', [
        mc('e5e-4-2-1', 'What`s the weather like? — It`s _____.', ['sun', 'sunny', 'sun is', 'rains'], 'sunny', 'Sun + ny.', 'Sunny = adjective form.'),
        mc('e5e-4-2-2', 'What helps the environment?', ['Littering', 'Recycling', 'Wasting water', 'Cutting trees'], 'Recycling', 'Reduces waste.', 'Recycling reduces waste and pollution.'),
        mc('e5e-4-2-3', 'Cutting down forests is called:', ['Pollution', 'Deforestation', 'Recycling', 'Reusing'], 'Deforestation', 'De + forest.', 'Deforestation = de + forest.'),
        tf('e5e-4-2-4', 'We should recycle to protect the planet.', 'True', 'Reduce waste.', 'True — recycling helps protect Earth.', mk=False),
    ]),

    lesson('en5-4-test', 'Test — Our Planet & Health', '## Test: Our Planet, Our Health & Future', [
        mc('t5e-4-1', 'Healthy food:', ['Candy', 'Fast food', 'Vegetables', 'Soda'], 'Vegetables', 'Healthy.', 'Vegetables.'),
        mc('t5e-4-2', 'I _____ ride a bike.', ['am', 'do', 'can', 'is'], 'can', 'Ability.', 'Can.'),
        mc('t5e-4-3', 'Recycling helps:', ['Pollute more', 'Protect environment', 'Cut trees', 'Use more plastic'], 'Protect environment', 'Less waste.', 'Recycling protects environment.'),
        mc('t5e-4-4', 'It`s _____ today (sun).', ['sun', 'sunny', 'sunning', 'sons'], 'sunny', 'Adjective.', 'Sunny.'),
        tf('t5e-4-5', 'We should plant more trees.', 'True', 'Helps environment.', 'True — trees absorb CO₂.', mk=False),
    ], is_test=True),
]),

]
