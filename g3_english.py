# -*- coding: utf-8 -*-
"""Grade 3 English — BRO 1:1: 4 теми / ~12 lessons + 4 tests."""

SUBJECT = [
    unit('en3-1', 'Me and Others at Home', [
        lesson('en3-1-1', 'Family & Numbers', '''## Family
| English | MK |
|---|---|
| mother / mum | мама |
| father / dad | татко |
| brother | брат |
| sister | сестра |
| grandmother | баба |
| grandfather | дедо |
| aunt | тетка |
| uncle | вујко |
| cousin | братучед |

### Possessive `s
- *My mother`s name is Maja.* — Името на мама ми е Маја.

## Numbers 1-100
1-10: one, two, three...
20 twenty, 30 thirty, 40 forty, 50 fifty, 60 sixty, 70 seventy, 80 eighty, 90 ninety, 100 one hundred

### Combinations
- 25 = twenty-five
- 47 = forty-seven''', [
            mc('e3en-1-1-1', '„Aunt“ е:', ['баба', 'тетка', 'мама', 'сестра'], 'тетка', 'Aunt.', 'Тетка.'),
            mc('e3en-1-1-2', '„Twenty“ е:', ['12', '20', '22', '30'], '20', 'Twenty.', '20.'),
            mc('e3en-1-1-3', '„Fifty“ е:', ['5', '15', '50', '500'], '50', 'Fifty.', '50.'),
            tf('e3en-1-1-4', '„Marko`s book“ значи „книгата на Марко“.', 'True', 'Possessive.', 'True.', mk=False),
        ]),
        lesson('en3-1-2', 'Home and Daily Routine', '''## Rooms
- bedroom, living room, kitchen, bathroom, dining room

### Furniture
- bed, table, chair, sofa, window, door

## Daily Routine

| English | MK |
|---|---|
| wake up | будам се |
| have breakfast | појадувам |
| go to school | одам в школа |
| have lunch | ручам |
| do homework | правам домашна |
| have dinner | вечерам |
| go to bed | одам на спиење |

### Sentence
- *I wake up at 7.* — Будам се во 7.
- *I have lunch at 1.*''', [
            mc('e3en-1-2-1', '„Wake up“ е:', ['Спијам', 'Будам се', 'Јадам', 'Играм'], 'Будам се', 'Wake up.', 'Будам се.'),
            mc('e3en-1-2-2', '„Bedroom“ е:', ['кујна', 'спална', 'двор', 'бања'], 'спална', 'Bed.', 'Спална.'),
            mc('e3en-1-2-3', '„Have lunch“ е:', ['појадок', 'ручок', 'вечера', 'спиење'], 'ручок', 'Lunch.', 'Ручок.'),
            tf('e3en-1-2-4', '„Have dinner“ значи „вечерам“.', 'True', 'Dinner.', 'True.', mk=False),
        ]),
        lesson('en3-1-test', 'Test — Home', '## Test: Family', [
            mc('t3en-1-1', '„Grandfather“ е:', ['баба', 'дедо', 'татко', 'вујко'], 'дедо', 'Grandfather.', 'Дедо.'),
            mc('t3en-1-2', '„Seventy“ е:', ['7', '17', '70', '700'], '70', 'Seventy.', '70.'),
            mc('t3en-1-3', '„Wake up“ е:', ['Спијам', 'Будам се', 'Јадам', 'Играм'], 'Будам се', 'Wake up.', 'Будам се.'),
            tf('t3en-1-4', '„Cousin“ значи братучед.', 'True', 'Cousin.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en3-2', 'Me and Others at School', [
        lesson('en3-2-1', 'School Things & Time', '''## School
| English | MK |
|---|---|
| school | училиште |
| teacher | наставник |
| pupil | ученик |
| classroom | училница |
| desk | клупа |
| book | книга |
| notebook | тетратка |
| pen | пенкало |
| pencil | молив |
| eraser | гумичка |
| ruler | линијар |

## Time

### What`s the time?
- It`s 8 o`clock.
- It`s half past 8 (8:30).
- It`s a quarter past 8 (8:15).
- It`s a quarter to 9 (8:45).''', [
            mc('e3en-2-1-1', '„Eraser“ е:', ['линијар', 'гумичка', 'молив', 'пенкало'], 'гумичка', 'Eraser.', 'Гумичка.'),
            mc('e3en-2-1-2', '„Half past 8“ е:', ['8:00', '8:15', '8:30', '8:45'], '8:30', 'Half=пол.', '8:30.'),
            mc('e3en-2-1-3', '„Ruler“ е:', ['линијар', 'гумичка', 'молив', 'пенкало'], 'линијар', 'Ruler.', 'Линијар.'),
            tf('e3en-2-1-4', '„Notebook“ значи „тетратка“.', 'True', 'Note-book.', 'True.', mk=False),
        ]),
        lesson('en3-2-2', 'Subjects, Days, Months', '''## Subjects
Maths, English, Macedonian, Art, Music, PE, Science

## Days of the Week
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

## Months
January, February, March, April, May, June, July, August, September, October, November, December

### Sentence
- *On Monday I have Maths.* — Во понеделник имам математика.
- *My birthday is in May.* — Мој роденден е во мај.''', [
            mc('e3en-2-2-1', '„Wednesday“ е:', ['понеделник', 'вторник', 'среда', 'четврток'], 'среда', 'Wednesday.', 'Среда.'),
            mc('e3en-2-2-2', '„December“ е:', ['јануари', 'март', 'мај', 'декември'], 'декември', 'December.', 'Декември.'),
            mc('e3en-2-2-3', '„Maths“ е:', ['Историја', 'Математика', 'Музичко', 'Англиски'], 'Математика', 'Maths.', 'Математика.'),
            tf('e3en-2-2-4', '„Sunday“ е недела.', 'True', 'Sun.', 'True.', mk=False),
        ]),
        lesson('en3-2-3', 'Polite Phrases', '''## Polite phrases
- Please — Молам
- Thank you — Благодарам
- Sorry — Извини
- Excuse me — Извини/повелете
- You`re welcome — Нема на што

### Asking
- Can I... ? — Можам ли... ?
- Could you... ? — Би можел/а да...?

### Examples
- *Can I have a pen, please?*
- *Thank you, teacher!*
- *Sorry, I am late.*
- *I don`t understand.*''', [
            mc('e3en-2-3-1', '„Please“ е:', ['Благодарам', 'Молам', 'Извини', 'Здраво'], 'Молам', 'Polite.', 'Молам.'),
            mc('e3en-2-3-2', '„I don`t understand“ значи:', ['Не знам', 'Не разбирам', 'Доцнам', 'Сум здрав'], 'Не разбирам', 'Understand.', 'Не разбирам.'),
            tf('e3en-2-3-3', '„Excuse me“ значи „Извини“.', 'True', 'Учтив.', 'True.', mk=False),
        ]),
        lesson('en3-2-test', 'Test — School', '## Test: School', [
            mc('t3en-2-1', '„Pencil“ е:', ['пенкало', 'молив', 'торба', 'клупа'], 'молив', 'Pencil.', 'Молив.'),
            mc('t3en-2-2', '„Friday“ е:', ['понеделник', 'четврток', 'петок', 'сабота'], 'петок', 'Friday.', 'Петок.'),
            mc('t3en-2-3', '„Please“ е:', ['Благодарам', 'Молам', 'Извини', 'Не'], 'Молам', 'Учтив.', 'Молам.'),
            tf('t3en-2-4', '„January“ е јануари.', 'True', 'January.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en3-3', 'Me and Others in My Environment', [
        lesson('en3-3-1', 'Animals & Plants', '''## Animals
| English | MK |
|---|---|
| dog | куче |
| cat | мачка |
| bird | птица |
| fish | риба |
| horse | коњ |
| cow | крава |
| pig | свиња |
| sheep | овца |
| rabbit | зајак |
| lion | лав |
| tiger | тигар |
| elephant | слон |
| monkey | мајмун |
| bear | мечка |

## Plants
- tree — дрво
- flower — цвет
- grass — трева
- leaf — лист''', [
            mc('e3en-3-1-1', '„Lion“ е:', ['куче', 'тигар', 'лав', 'мечка'], 'лав', 'Lion.', 'Лав.'),
            mc('e3en-3-1-2', '„Tree“ е:', ['цвет', 'дрво', 'трева', 'птица'], 'дрво', 'Tree.', 'Дрво.'),
            mc('e3en-3-1-3', '„Birds fly“ значи:', ['Птици пливаат', 'Птици летаат', 'Птици трчаат', 'Птици јадат'], 'Птици летаат', 'Fly.', 'Птици летаат.'),
            tf('e3en-3-1-4', '„Elephant“ значи „слон“.', 'True', 'Elephant.', 'True.', mk=False),
        ]),
        lesson('en3-3-2', 'Weather & Seasons', '''## Weather
- sunny, cloudy, rainy, snowy, windy, stormy
- hot, warm, cool, cold

## Seasons
- spring — пролет
- summer — лето
- autumn — есен
- winter — зима

### Sentence
- *It`s sunny today.* — Денеска е сончево.
- *In winter it`s cold.* — Во зима е студено.
- *I love summer.* — Сакам лето.''', [
            mc('e3en-3-2-1', '„Summer“ е:', ['пролет', 'лето', 'есен', 'зима'], 'лето', 'Summer.', 'Лето.'),
            mc('e3en-3-2-2', '„Snowy“ е:', ['сончев', 'дождлив', 'снежен', 'облачен'], 'снежен', 'Snow.', 'Снежен.'),
            mc('e3en-3-2-3', '„Cold“ е:', ['топло', 'студено', 'мокро', 'суво'], 'студено', 'Cold.', 'Студено.'),
            tf('e3en-3-2-4', '„Autumn“ значи „есен“.', 'True', 'Autumn.', 'True.', mk=False),
        ]),
        lesson('en3-3-3', 'Places in Town', '''## Places
- school, hospital, park, shop, library, cinema, post office
- restaurant, zoo, museum, bank
- church, mosque

## My town
- *I live in Skopje.* — Живеам во Скопје.
- *Skopje is the capital of Macedonia.* — Скопје е главен град на Македонија.

## Directions
- left — лево
- right — десно
- straight on — право
- next to — до

### Asking
- *Where is the park?* — Каде е паркот?''', [
            mc('e3en-3-3-1', '„Park“ е:', ['училиште', 'парк', 'продавница', 'болница'], 'парк', 'Park.', 'Парк.'),
            mc('e3en-3-3-2', '„Cinema“ е:', ['училиште', 'кино', 'парк', 'болница'], 'кино', 'Films.', 'Кино.'),
            mc('e3en-3-3-3', '„Turn left“ е:', ['Сврти десно', 'Сврти лево', 'Оди право', 'Стоп'], 'Сврти лево', 'Left.', 'Сврти лево.'),
            tf('e3en-3-3-4', '„Skopje is the capital of Macedonia“.', 'True', 'Главен град.', 'True.', mk=False),
        ]),
        lesson('en3-3-test', 'Test — Environment', '## Test: Environment', [
            mc('t3en-3-1', '„Elephant“ е:', ['тигар', 'мечка', 'слон', 'лав'], 'слон', 'Elephant.', 'Слон.'),
            mc('t3en-3-2', '„Winter“ е:', ['пролет', 'лето', 'есен', 'зима'], 'зима', 'Winter.', 'Зима.'),
            mc('t3en-3-3', '„Cinema“ е:', ['училиште', 'кино', 'парк', 'болница'], 'кино', 'Films.', 'Кино.'),
            tf('t3en-3-4', '„Hot“ значи „топло“.', 'True', 'Hot.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en3-4', 'Me and Others in Free Time', [
        lesson('en3-4-1', 'Activities & CAN', '''## Activities
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
| cook | готвам |
| watch TV | гледам ТВ |
| listen to music | слушам музика |

## „I can / can`t“

- *I can swim.* — Можам да пливам.
- *I can`t fly.* — Не можам да летам.
- *Can you ride a bike?* — Можеш ли да возиш велосипед?

### „I like + verb-ing“
- *I like reading.* — Сакам да читам.
- *I like playing football.* — Сакам да играм фудбал.''', [
            mc('e3en-4-1-1', '„Cook“ е:', ['пеам', 'готвам', 'трчам', 'спијам'], 'готвам', 'Cook.', 'Готвам.'),
            mc('e3en-4-1-2', '„I can swim“ значи:', ['Не можам пливам', 'Можам пливам', 'Сакам пливам', 'Мразам пливам'], 'Можам пливам', 'Can.', 'Можам.'),
            mc('e3en-4-1-3', '„Watch TV“ е:', ['гледам ТВ', 'слушам музика', 'читам', 'играм'], 'гледам ТВ', 'Watch.', 'Гледам ТВ.'),
            tf('e3en-4-1-4', '„I like reading“ значи „Сакам да читам“.', 'True', 'Like.', 'True.', mk=False),
        ]),
        lesson('en3-4-2', 'Sports & Toys', '''## Sports
- football, basketball, tennis, volleyball
- swimming, running, cycling

### Verbs
- **play** with team sports: play football
- **go** with -ing: go swimming
- **do** with martial arts: do karate

## Toys
- ball, doll, car (играчка), bike, teddy bear, puzzle, game

### „I have...“
- *I have a red ball.* — Имам црвена топка.

### „Let`s play!“
- *Let`s play football!* — Ајде да играме фудбал!''', [
            mc('e3en-4-2-1', 'Со спортови со топка:', ['play', 'go', 'do', 'make'], 'play', 'Play football.', 'Play.'),
            mc('e3en-4-2-2', '„Ball“ е:', ['кукла', 'топка', 'автомобил', 'велосипед'], 'топка', 'Ball.', 'Топка.'),
            mc('e3en-4-2-3', '„Cycling“ е:', ['танцување', 'пливање', 'возење велосипед', 'трчање'], 'возење велосипед', 'Cycle.', 'Велосипед.'),
            tf('e3en-4-2-4', '„Tennis“ значи „тенис“.', 'True', 'Tennis.', 'True.', mk=False),
        ]),
        lesson('en3-4-3', 'Hobbies & Free Time', '''## Hobbies

### My favourite...
- *My favourite sport is football.* — Мој омилен спорт е фудбал.
- *My favourite food is pizza.* — Моја омилена храна е пица.
- *My favourite colour is blue.* — Моја омилена боја е сино.

### Free time
- *In my free time, I play with friends.*
- *I read books in the evening.*
- *On weekends, I watch films.*

### Time of day
- morning, afternoon, evening, night
- in the morning, in the afternoon
- on Saturday / Sunday
- at the weekend''', [
            mc('e3en-4-3-1', '„My favourite colour is blue“ значи:', ['Боја се` едно', 'Моја омилена боја е сино', 'Не сакам сино', 'Боја е жолто'], 'Моја омилена боја е сино', 'Favourite.', 'Омилена.'),
            mc('e3en-4-3-2', '„Weekend“ е:', ['Школски ден', 'Сабота и недела', 'Понеделник', 'Празник'], 'Сабота и недела', 'Викенд.', 'Викенд.'),
            mc('e3en-4-3-3', '„In the morning“ е:', ['Наутро', 'Попладне', 'Навечер', 'Ноќе'], 'Наутро', 'Morning.', 'Наутро.'),
            tf('e3en-4-3-4', '„Free time“ значи „слободно време“.', 'True', 'Free.', 'True.', mk=False),
        ]),
        lesson('en3-4-test', 'Test — Free Time', '## Test: Free time', [
            mc('t3en-4-1', '„Draw“ е:', ['пеам', 'танцувам', 'цртам', 'спијам'], 'цртам', 'Draw.', 'Цртам.'),
            mc('t3en-4-2', '„I can read“ значи:', ['Не можам читам', 'Можам читам', 'Сакам читам', 'Мразам читам'], 'Можам читам', 'Can.', 'Можам.'),
            mc('t3en-4-3', '„Football“ значи:', ['Фудбал', 'Кошарка', 'Тенис', 'Пливање'], 'Фудбал', 'Football.', 'Фудбал.'),
            tf('t3en-4-4', '„Weekend“ е „сабота и недела“.', 'True', 'Weekend.', 'True.', mk=False),
        ], is_test=True),
    ]),
]
