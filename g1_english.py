# -*- coding: utf-8 -*-
"""Grade 1 English — BRO 1:1: 4 теми / 12 lessons + 4 tests."""

SUBJECT = [
    unit('en1-1', 'Me and Others at Home', [
        lesson('en1-1-1', 'Hello! Greetings', '''## Greetings

| English | MK |
|---|---|
| Hello | Здраво |
| Hi | Чао (поздрав) |
| Good morning | Добро утро |
| Good afternoon | Добар ден |
| Good night | Добра ноќ |
| Goodbye / Bye | Довидување / Чао |

### Polite words
- **Please** — молам
- **Thank you** — благодарам
- **You`re welcome** — нема на што
- **Sorry** — извини

### Introducing yourself
- *My name is Marko.* — Се викам Марко.
- *I am 7.* — Имам 7 години.

### Yes / No
- **Yes** — да
- **No** — не''', [
            mc('e1en-1-1-1', '„Hello“ значи:', ['Чао', 'Здраво', 'Благодарам', 'Не'], 'Здраво', 'Поздрав.', 'Здраво.'),
            mc('e1en-1-1-2', '„Thank you“ значи:', ['Молам', 'Благодарам', 'Извини', 'Не'], 'Благодарам', 'Учтиво.', 'Благодарам.'),
            mc('e1en-1-1-3', '„Good night“ значи:', ['Добро утро', 'Добар ден', 'Добра ноќ', 'Здраво'], 'Добра ноќ', 'Night = ноќ.', 'Добра ноќ.'),
            tf('e1en-1-1-4', '„Yes“ значи „да“.', 'True', 'Y = да.', 'True.', mk=False),
        ]),
        lesson('en1-1-2', 'My Family', '''## Family

| English | MK |
|---|---|
| mum / mother | мама |
| dad / father | татко |
| brother | брат |
| sister | сестра |
| grandma | баба |
| grandpa | дедо |

### Sentence
- *This is my mum.* — Ова е мама ми.
- *This is my brother.* — Ова е брат ми.

### Family pets
- **dog** — куче
- **cat** — мачка
- **bird** — птица
- **fish** — риба

### „I have...“
- *I have a brother.* — Имам брат.
- *I have a dog.* — Имам куче.

### „I love...“
- *I love my family.* — Ја сакам моето семејство.
- *I love my dog.* — Го сакам моето куче.''', [
            mc('e1en-1-2-1', '„Mother“ е:', ['татко', 'мама', 'брат', 'сестра'], 'мама', 'Mother.', 'Мама.'),
            mc('e1en-1-2-2', '„Dog“ е:', ['мачка', 'куче', 'птица', 'риба'], 'куче', 'Dog.', 'Куче.'),
            mc('e1en-1-2-3', '„Sister“ е:', ['брат', 'сестра', 'баба', 'тетка'], 'сестра', 'Sister.', 'Сестра.'),
            tf('e1en-1-2-4', '„I love my family“ значи „Ја сакам семејството“.', 'True', 'Love = сака.', 'True.', mk=False),
        ]),
        lesson('en1-1-3', 'Numbers 1-10 & Colors', '''## Numbers 1-10

| Number | English | MK |
|---|---|---|
| 1 | one | еден |
| 2 | two | два |
| 3 | three | три |
| 4 | four | четири |
| 5 | five | пет |
| 6 | six | шест |
| 7 | seven | седум |
| 8 | eight | осум |
| 9 | nine | девет |
| 10 | ten | десет |

### „I am X“
- *I am 7.* — Имам 7 години.
- *I am 8.* — Имам 8 години.

## Colors

| English | MK |
|---|---|
| red | црвено |
| blue | сино |
| green | зелено |
| yellow | жолто |
| black | црно |
| white | бело |
| pink | розово |
| orange | портокалово |

### Sentence
- *I like blue.* — Ми се допаѓа сино.
- *My ball is red.* — Топката ми е црвена.''', [
            mc('e1en-1-3-1', '„Five“ е:', ['3', '4', '5', '6'], '5', 'Five = 5.', '5.'),
            mc('e1en-1-3-2', '„Red“ е:', ['сино', 'црвено', 'зелено', 'жолто'], 'црвено', 'Red.', 'Црвено.'),
            mc('e1en-1-3-3', '„Eight“ е:', ['6', '7', '8', '9'], '8', 'Eight.', '8.'),
            tf('e1en-1-3-4', '„Blue“ значи „сино“.', 'True', 'Blue = сино.', 'True.', mk=False),
        ]),
        lesson('en1-1-test', 'Test — Home', '## Test: Me and others at home', [
            mc('t1en-1-1', '„Father“ е:', ['мама', 'татко', 'брат', 'сестра'], 'татко', 'Father.', 'Татко.'),
            mc('t1en-1-2', '„Three“ е:', ['1', '2', '3', '4'], '3', 'Three.', '3.'),
            mc('t1en-1-3', '„Yellow“ е:', ['жолто', 'црвено', 'сино', 'зелено'], 'жолто', 'Yellow.', 'Жолто.'),
            tf('t1en-1-4', '„Please“ значи „Молам“.', 'True', 'Учтив.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en1-2', 'Me and Others at School', [
        lesson('en1-2-1', 'School Things', '''## School

| English | MK |
|---|---|
| school | училиште |
| classroom | училница |
| teacher | наставник |
| pupil | ученик |

### Things I have in school
- **book** — книга
- **notebook** — тетратка
- **pen** — пенкало
- **pencil** — молив
- **eraser** — гумичка
- **ruler** — линијар
- **bag** — торба

### Sentence: I have...
- *I have a pen.* — Имам пенкало.
- *I have a red book.* — Имам црвена книга.

### Question: What`s this?
- *What`s this?* — Што е ова?
- *It`s a pencil.* — Тоа е молив.
- *It`s a bag.* — Тоа е торба.''', [
            mc('e1en-2-1-1', '„Book“ е:', ['тетратка', 'книга', 'молив', 'торба'], 'книга', 'Book.', 'Книга.'),
            mc('e1en-2-1-2', '„Pencil“ е:', ['пенкало', 'молив', 'гумичка', 'линијар'], 'молив', 'Pencil.', 'Молив.'),
            mc('e1en-2-1-3', '„Teacher“ е:', ['ученик', 'наставник', 'книга', 'торба'], 'наставник', 'Teacher.', 'Наставник.'),
            tf('e1en-2-1-4', '„Bag“ значи „торба“.', 'True', 'Bag.', 'True.', mk=False),
        ]),
        lesson('en1-2-2', 'Polite Phrases at School', '''## Polite phrases

At school we use polite words:

- *Please* — Молам
- *Thank you* — Благодарам
- *Sorry* — Извини
- *Excuse me* — Извини / повелете

### Examples
- *Please, can I have a pen?* — Молам, можам ли пенкало?
- *Thank you, teacher!* — Благодарам, наставник!
- *Sorry, I am late.* — Извини, доцнам.

### Asking questions
- *Can I... ?* — Можам ли... ?
- *Can I go to the toilet?* — Можам ли да одам во тоалет?
- *Can I help you?* — Можам ли да ти помогнам?

### Common school sentences
- *I don`t know.* — Не знам.
- *I don`t understand.* — Не разбирам.
- *Please, repeat.* — Молам, повтори.''', [
            mc('e1en-2-2-1', '„Please“ е:', ['Благодарам', 'Молам', 'Извини', 'Здраво'], 'Молам', 'Polite.', 'Молам.'),
            mc('e1en-2-2-2', 'Кога не разбирам кажувам:', ['I don`t know', 'I don`t understand', 'I am late', 'Goodbye'], 'I don`t understand', 'Don`t understand.', 'I don`t understand.'),
            mc('e1en-2-2-3', '„Thank you“ кога:', ['Доцнам', 'Ми се даде нешто', 'Не знам', 'Сум здрав'], 'Ми се даде нешто', 'Учтив одговор.', 'Кога добиеме.', ),
            tf('e1en-2-2-4', '„Excuse me“ значи „Извини“.', 'True', 'Учтив.', 'True.', mk=False),
        ]),
        lesson('en1-2-3', 'Subjects at School', '''## School Subjects

| English | MK |
|---|---|
| Maths | Математика |
| English | Англиски |
| Macedonian | Македонски |
| Art | Ликовно |
| Music | Музичко |
| PE (Physical Education) | Физичко |
| Science | Природни науки |

### Days of the Week
- **Monday** — понеделник
- **Tuesday** — вторник
- **Wednesday** — среда
- **Thursday** — четврток
- **Friday** — петок
- **Saturday** — сабота
- **Sunday** — недела

### „On Monday I have...“
- *On Monday I have Maths.* — Во понеделник имам математика.
- *On Wednesday I have English.* — Во среда имам англиски.

### Question: „What do you have today?“
- *What do you have today?* — Што имаш денеска?
- *I have Maths and English.* — Имам математика и англиски.''', [
            mc('e1en-2-3-1', '„Maths“ е:', ['Историја', 'Математика', 'Музичко', 'Англиски'], 'Математика', 'Maths.', 'Математика.'),
            mc('e1en-2-3-2', '„Friday“ е:', ['понеделник', 'четврток', 'петок', 'сабота'], 'петок', 'Friday.', 'Петок.'),
            mc('e1en-2-3-3', '„Sunday“ е:', ['понеделник', 'сабота', 'недела', 'петок'], 'недела', 'Sunday.', 'Недела.'),
            tf('e1en-2-3-4', '„Music“ значи „Музичко“.', 'True', 'Music.', 'True.', mk=False),
        ]),
        lesson('en1-2-test', 'Test — School', '## Test: Me and others at school', [
            mc('t1en-2-1', '„Pencil“ е:', ['пенкало', 'молив', 'гумичка', 'торба'], 'молив', 'Pencil.', 'Молив.'),
            mc('t1en-2-2', '„Wednesday“ е:', ['понеделник', 'вторник', 'среда', 'четврток'], 'среда', 'Wednesday.', 'Среда.'),
            mc('t1en-2-3', '„Please“ е:', ['Благодарам', 'Молам', 'Извини', 'Не'], 'Молам', 'Учтив.', 'Молам.'),
            tf('t1en-2-4', '„Music“ значи „Музичко“.', 'True', 'Music.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en1-3', 'Me and Others in My Environment', [
        lesson('en1-3-1', 'Animals', '''## Animals

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
| rabbit | зајак |
| chicken | пиле |
| duck | патка |

### Wild animals
- **lion** — лав
- **tiger** — тигар
- **elephant** — слон
- **monkey** — мајмун
- **bear** — мечка

### What do animals do?
- *Dogs run.* — Кучињата трчаат.
- *Birds fly.* — Птиците летаат.
- *Fish swim.* — Рибите пливаат.
- *Cats jump.* — Мачките скокаат.

### Sound of animals
- Dog: *woof woof*
- Cat: *meow*
- Cow: *moo*
- Sheep: *baa*''', [
            mc('e1en-3-1-1', '„Cat“ е:', ['куче', 'мачка', 'риба', 'птица'], 'мачка', 'Cat.', 'Мачка.'),
            mc('e1en-3-1-2', '„Birds fly“ значи:', ['Птици пливаат', 'Птици летаат', 'Птици трчаат', 'Птици јадат'], 'Птици летаат', 'Fly = летаат.', 'Птици летаат.'),
            mc('e1en-3-1-3', '„Lion“ е:', ['куче', 'тигар', 'лав', 'мечка'], 'лав', 'Lion.', 'Лав.'),
            tf('e1en-3-1-4', '„Elephant“ значи „слон“.', 'True', 'Elephant.', 'True.', mk=False),
        ]),
        lesson('en1-3-2', 'Nature & Weather', '''## Nature

| English | MK |
|---|---|
| sun | сонце |
| moon | месечина |
| star | ѕвезда |
| sky | небо |
| tree | дрво |
| flower | цвет |
| grass | трева |
| water | вода |
| rain | дожд |
| snow | снег |
| wind | ветер |

### Weather
| English | MK |
|---|---|
| sunny | сончев |
| cloudy | облачен |
| rainy | дождлив |
| snowy | снежен |
| windy | ветровит |
| hot | топло |
| cold | студено |

### „It`s ___ today“
- *It`s sunny today.* — Денеска е сончево.
- *It`s rainy.* — Дождливо е.
- *It`s cold.* — Студено е.''', [
            mc('e1en-3-2-1', '„Sun“ е:', ['месечина', 'сонце', 'ѕвезда', 'дрво'], 'сонце', 'Sun.', 'Сонце.'),
            mc('e1en-3-2-2', '„Sunny“ е:', ['сончев', 'дождлив', 'снежен', 'облачен'], 'сончев', 'Sun.', 'Сончев.'),
            mc('e1en-3-2-3', '„Cold“ е:', ['топло', 'студено', 'мокро', 'суво'], 'студено', 'Cold.', 'Студено.'),
            tf('e1en-3-2-4', '„Tree“ значи „дрво“.', 'True', 'Tree.', 'True.', mk=False),
        ]),
        lesson('en1-3-3', 'Places in My Town', '''## Places

| English | MK |
|---|---|
| home / house | дом / куќа |
| school | училиште |
| park | парк |
| shop | продавница |
| hospital | болница |
| zoo | зоолошка градина |
| cinema | кино |

### Sentence: I go to...
- *I go to school.* — Одам в училиште.
- *I go to the park.* — Одам в парк.
- *Mum goes to the shop.* — Мама оди в продавница.

### My town
- *I live in Skopje.* — Живеам во Скопје.
- *My city is Skopje.* — Мој град е Скопје.

### Macedonia
- *I am from Macedonia.* — Од Македонија сум.
- *Macedonia is beautiful.* — Македонија е убава.

### „Where is...?“
- *Where is the park?* — Каде е паркот?
- *It`s near the school.* — Близу е училиштето.''', [
            mc('e1en-3-3-1', '„Park“ е:', ['училиште', 'парк', 'продавница', 'болница'], 'парк', 'Park.', 'Парк.'),
            mc('e1en-3-3-2', '„Shop“ е:', ['училиште', 'парк', 'продавница', 'кино'], 'продавница', 'Shop.', 'Продавница.'),
            mc('e1en-3-3-3', '„I go to school“ значи:', ['Дома сум', 'Одам в училиште', 'Сакам школа', 'Бегам'], 'Одам в училиште', 'Go to school.', 'Одам в училиште.'),
            tf('e1en-3-3-4', '„I live in Skopje“ значи „Живеам во Скопје“.', 'True', 'Live.', 'True.', mk=False),
        ]),
        lesson('en1-3-test', 'Test — Environment', '## Test: My environment', [
            mc('t1en-3-1', '„Bird“ е:', ['риба', 'куче', 'птица', 'крава'], 'птица', 'Bird.', 'Птица.'),
            mc('t1en-3-2', '„Water“ е:', ['снег', 'вода', 'оган', 'дрво'], 'вода', 'Water.', 'Вода.'),
            mc('t1en-3-3', '„Sunny“ е:', ['сончев', 'дождлив', 'снежен', 'облачен'], 'сончев', 'Sun.', 'Сончев.'),
            tf('t1en-3-4', '„Flower“ значи „цвет“.', 'True', 'Flower.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en1-4', 'Me and Others in Free Time', [
        lesson('en1-4-1', 'Activities', '''## Activities

| English | MK |
|---|---|
| play | играм |
| run | трчам |
| jump | скокам |
| swim | пливам |
| dance | танцувам |
| sing | пеам |
| read | читам |
| draw | цртам |
| write | пишувам |
| eat | јадам |
| drink | пијам |
| sleep | спијам |
| watch TV | гледам ТВ |

### „I like...“
- *I like to play.* — Сакам да играм.
- *I like to swim.* — Сакам да пливам.

### Sports
- **football** — фудбал
- **basketball** — кошарка
- **tennis** — тенис

### „I can / I can`t“
- *I can swim.* — Можам да пливам.
- *I can`t fly.* — Не можам да летам.''', [
            mc('e1en-4-1-1', '„Read“ е:', ['пиша', 'читам', 'цртам', 'спијам'], 'читам', 'Read.', 'Читам.'),
            mc('e1en-4-1-2', '„Swim“ е:', ['танцувам', 'пеам', 'пливам', 'трчам'], 'пливам', 'Swim.', 'Пливам.'),
            mc('e1en-4-1-3', '„I can swim“ значи:', ['Не можам пливам', 'Можам пливам', 'Сакам пливам', 'Мразам пливам'], 'Можам пливам', 'Can.', 'Можам.'),
            tf('e1en-4-1-4', '„I like to play“ значи „Сакам да играм“.', 'True', 'Like.', 'True.', mk=False),
        ]),
        lesson('en1-4-2', 'Toys & Games', '''## Toys

| English | MK |
|---|---|
| ball | топка |
| doll | кукла |
| car | автомобил (играчка) |
| bike | велосипед |
| teddy bear | плишано меченце |
| puzzle | сложувалка |
| game | игра |

### „I have / I don`t have“
- *I have a ball.* — Имам топка.
- *I don`t have a doll.* — Немам кукла.

### Sharing
- *Can I play with you?* — Можам ли да играм со тебе?
- *Yes, you can.* — Да, можеш.
- *Let`s play together!* — Ајде да играме заедно!

### Games
- **hide and seek** — криенка
- **tag** — гонење
- **board game** — игра на табла

### Friends
- *Marko is my friend.* — Марко е мој пријател.
- *Let`s be friends.* — Ајде да бидеме пријатели.''', [
            mc('e1en-4-2-1', '„Ball“ е:', ['кукла', 'топка', 'автомобил', 'велосипед'], 'топка', 'Ball.', 'Топка.'),
            mc('e1en-4-2-2', '„Bike“ е:', ['топка', 'кукла', 'велосипед', 'кутија'], 'велосипед', 'Bike.', 'Велосипед.'),
            mc('e1en-4-2-3', '„Hide and seek“ е:', ['Гонење', 'Криенка', 'Игра на табла', 'Шах'], 'Криенка', 'Сокривање.', 'Криенка.'),
            tf('e1en-4-2-4', '„Friend“ значи „пријател“.', 'True', 'Friend.', 'True.', mk=False),
        ]),
        lesson('en1-4-3', 'My Day', '''## My Day

### Morning
- *I wake up.* — Будам се.
- *I have breakfast.* — Појадувам.
- *I go to school.* — Одам в училиште.

### Afternoon
- *I have lunch.* — Ручам.
- *I do homework.* — Правам домашна.
- *I play.* — Играм.

### Evening
- *I have dinner.* — Вечерам.
- *I watch TV.* — Гледам ТВ.
- *I read a book.* — Читам книга.

### Night
- *I go to bed.* — Одам на спиење.
- *I sleep.* — Спијам.

### Time expressions
- in the morning — наутро
- in the afternoon — попладне
- in the evening — навечер
- at night — ноќе

### „What time is it?“
- *It`s 8 o`clock.* — 8 часот е.''', [
            mc('e1en-4-3-1', '„I wake up“ значи:', ['Спијам', 'Будам се', 'Јадам', 'Играм'], 'Будам се', 'Wake up.', 'Будам се.'),
            mc('e1en-4-3-2', '„Breakfast“ е:', ['Појадок', 'Ручок', 'Вечера', 'Ужина'], 'Појадок', 'Breakfast.', 'Појадок.'),
            mc('e1en-4-3-3', '„In the evening“ значи:', ['Наутро', 'Попладне', 'Навечер', 'Ноќе'], 'Навечер', 'Evening.', 'Навечер.'),
            tf('e1en-4-3-4', '„I go to bed“ значи „Одам на спиење“.', 'True', 'Bed = кревет.', 'True.', mk=False),
        ]),
        lesson('en1-4-test', 'Test — Free Time', '## Test: Free time', [
            mc('t1en-4-1', '„Run“ е:', ['пеам', 'танцувам', 'трчам', 'спијам'], 'трчам', 'Run.', 'Трчам.'),
            mc('t1en-4-2', '„Car“ е:', ['кукла', 'топка', 'автомобил', 'велосипед'], 'автомобил', 'Car.', 'Автомобил.'),
            mc('t1en-4-3', '„I sleep“ значи:', ['Играм', 'Спијам', 'Јадам', 'Трчам'], 'Спијам', 'Sleep.', 'Спијам.'),
            tf('t1en-4-4', '„Breakfast“ е „појадок“.', 'True', 'Breakfast.', 'True.', mk=False),
        ], is_test=True),
    ]),
]
