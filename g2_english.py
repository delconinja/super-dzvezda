# -*- coding: utf-8 -*-
"""Grade 2 English — BRO 1:1: 4 теми / ~12 lessons + 4 tests."""

SUBJECT = [
    unit('en2-1', 'Me and Others at Home', [
        lesson('en2-1-1', 'Family & Greetings', '''## Greetings
| English | MK |
|---|---|
| Hello / Hi | Здраво |
| Good morning | Добро утро |
| Good afternoon | Добар ден |
| Good night | Добра ноќ |
| Goodbye / Bye | Чао |

## Family
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

### Introducing
- *My name is Marko.* — Се викам Марко.
- *I am 8 years old.*''', [
            mc('e2en-1-1-1', '„Mother“ е:', ['татко', 'мама', 'брат', 'сестра'], 'мама', 'Mother.', 'Мама.'),
            mc('e2en-1-1-2', '„Aunt“ е:', ['баба', 'тетка', 'мама', 'сестра'], 'тетка', 'Aunt.', 'Тетка.'),
            mc('e2en-1-1-3', '„Good night“ е:', ['Добро утро', 'Добар ден', 'Добра ноќ', 'Чао'], 'Добра ноќ', 'Night.', 'Добра ноќ.'),
            tf('e2en-1-1-4', '„Brother“ значи „брат“.', 'True', 'Brother.', 'True.', mk=False),
        ]),
        lesson('en2-1-2', 'Numbers 1-20', '''## Numbers 1-10
one, two, three, four, five, six, seven, eight, nine, ten

## Numbers 11-20
eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty

### Age
- *I am 8 years old.* — Имам 8 години.
- *I am 8.* — Имам 8.

### „How old are you?“
- *How old are you?* — Колку години имаш?
- *I am 8.*''', [
            mc('e2en-1-2-1', '„Eight“ е:', ['6', '7', '8', '9'], '8', 'Eight.', '8.'),
            mc('e2en-1-2-2', '„Fifteen“ е:', ['5', '14', '15', '50'], '15', 'Fifteen.', '15.'),
            mc('e2en-1-2-3', '„Twenty“ е:', ['12', '20', '22', '30'], '20', 'Twenty.', '20.'),
            tf('e2en-1-2-4', '„I am 8 years old“ значи „Имам 8 години“.', 'True', 'Age.', 'True.', mk=False),
        ]),
        lesson('en2-1-3', 'House and Rooms', '''## House Rooms
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
| window | прозорец |
| door | врата |

### Sentence: This is...
- *This is my bedroom.* — Ова е моја спална.
- *I have a big bed.* — Имам голем кревет.''', [
            mc('e2en-1-3-1', 'Каде спиеш?', ['kitchen', 'bedroom', 'garden', 'living room'], 'bedroom', 'Bed.', 'Bedroom.'),
            mc('e2en-1-3-2', '„Window“ е:', ['врата', 'прозорец', 'стол', 'маса'], 'прозорец', 'Window.', 'Прозорец.'),
            mc('e2en-1-3-3', '„Garden“ е:', ['кујна', 'двор', 'бања', 'спална'], 'двор', 'Garden.', 'Двор.'),
            tf('e2en-1-3-4', '„Kitchen“ е „кујна“.', 'True', 'Kitchen.', 'True.', mk=False),
        ]),
        lesson('en2-1-test', 'Test — Home', '## Test: Home', [
            mc('t2en-1-1', '„Sister“ е:', ['брат', 'сестра', 'тетка', 'баба'], 'сестра', 'Sister.', 'Сестра.'),
            mc('t2en-1-2', '„Twenty“ е:', ['2', '20', '12', '22'], '20', 'Twenty.', '20.'),
            mc('t2en-1-3', '„Bedroom“ е:', ['кујна', 'спална', 'двор', 'бања'], 'спална', 'Bed.', 'Спална.'),
            tf('t2en-1-4', '„Uncle“ значи „вујко“.', 'True', 'Uncle.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en2-2', 'Me and Others at School', [
        lesson('en2-2-1', 'School Things', '''## School Vocabulary
| English | MK |
|---|---|
| school | училиште |
| classroom | училница |
| teacher | наставник |
| pupil | ученик |
| desk | клупа |
| board | табла |
| book | книга |
| notebook | тетратка |
| pen | пенкало |
| pencil | молив |
| ruler | линијар |
| bag | торба |

### Sentence: I have...
- *I have a pen.* — Имам пенкало.
- *I have a red book.* — Имам црвена книга.''', [
            mc('e2en-2-1-1', '„Notebook“ е:', ['книга', 'тетратка', 'клупа', 'торба'], 'тетратка', 'Note-book.', 'Тетратка.'),
            mc('e2en-2-1-2', '„Teacher“ е:', ['ученик', 'наставник', 'книга', 'торба'], 'наставник', 'Teacher.', 'Наставник.'),
            mc('e2en-2-1-3', '„Pen“ е:', ['пенкало', 'молив', 'линијар', 'клупа'], 'пенкало', 'Pen.', 'Пенкало.'),
            tf('e2en-2-1-4', '„Ruler“ значи „линијар“.', 'True', 'Ruler.', 'True.', mk=False),
        ]),
        lesson('en2-2-2', 'Colors', '''## Colors
| English | MK |
|---|---|
| red | црвено |
| blue | сино |
| green | зелено |
| yellow | жолто |
| orange | портокалово |
| purple | виолетово |
| pink | розово |
| brown | кафено |
| black | црно |
| white | бело |

### Sentence: It`s...
- *My book is red.* — Книгата ми е црвена.
- *The sky is blue.* — Небото е сино.''', [
            mc('e2en-2-2-1', '„Orange“ е:', ['црвено', 'жолто', 'портокалово', 'кафено'], 'портокалово', 'Orange.', 'Портокалово.'),
            mc('e2en-2-2-2', '„White“ е:', ['црно', 'бело', 'жолто', 'црвено'], 'бело', 'White.', 'Бело.'),
            mc('e2en-2-2-3', '„Green“ е:', ['жолто', 'зелено', 'сино', 'црно'], 'зелено', 'Green.', 'Зелено.'),
            tf('e2en-2-2-4', '„Pink“ значи „розово“.', 'True', 'Pink.', 'True.', mk=False),
        ]),
        lesson('en2-2-3', 'Days & Subjects', '''## Days of the Week
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

| English | MK |
|---|---|
| Monday | понеделник |
| Tuesday | вторник |
| Wednesday | среда |
| Thursday | четврток |
| Friday | петок |
| Saturday | сабота |
| Sunday | недела |

## Subjects
- **Maths** — математика
- **English** — англиски
- **Macedonian** — македонски
- **Art** — ликовно
- **Music** — музичко
- **PE** — физичко
- **Science** — природни науки

### Sentence
- *On Monday I have Maths.* — Во понеделник имам математика.''', [
            mc('e2en-2-3-1', '„Friday“ е:', ['понеделник', 'четврток', 'петок', 'сабота'], 'петок', 'Friday.', 'Петок.'),
            mc('e2en-2-3-2', '„Maths“ е:', ['Историја', 'Математика', 'Музичко', 'Англиски'], 'Математика', 'Maths.', 'Математика.'),
            mc('e2en-2-3-3', '„Sunday“ е:', ['понеделник', 'недела', 'сабота', 'четврток'], 'недела', 'Sunday.', 'Недела.'),
            tf('e2en-2-3-4', '„Music“ значи „музичко“.', 'True', 'Music.', 'True.', mk=False),
        ]),
        lesson('en2-2-test', 'Test — School', '## Test: School', [
            mc('t2en-2-1', '„Pen“ е:', ['пенкало', 'молив', 'торба', 'клупа'], 'пенкало', 'Pen.', 'Пенкало.'),
            mc('t2en-2-2', '„Yellow“ е:', ['жолто', 'црвено', 'зелено', 'сино'], 'жолто', 'Yellow.', 'Жолто.'),
            mc('t2en-2-3', '„Wednesday“ е:', ['среда', 'петок', 'понеделник', 'недела'], 'среда', 'Wednesday.', 'Среда.'),
            tf('t2en-2-4', '„Bag“ значи „торба“.', 'True', 'Bag.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en2-3', 'Me and Others in My Environment', [
        lesson('en2-3-1', 'Animals', '''## Animals
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
| chicken | пиле |
| duck | патка |

### Wild
- **lion** — лав
- **tiger** — тигар
- **elephant** — слон
- **monkey** — мајмун
- **bear** — мечка

### „I see...“
- *I see a dog.* — Гледам куче.''', [
            mc('e2en-3-1-1', '„Horse“ е:', ['куче', 'коњ', 'крава', 'свиња'], 'коњ', 'Horse.', 'Коњ.'),
            mc('e2en-3-1-2', '„Lion“ е:', ['куче', 'тигар', 'лав', 'мечка'], 'лав', 'Lion.', 'Лав.'),
            mc('e2en-3-1-3', '„Cow“ е:', ['свиња', 'крава', 'овца', 'коњ'], 'крава', 'Cow.', 'Крава.'),
            tf('e2en-3-1-4', '„Elephant“ значи „слон“.', 'True', 'Elephant.', 'True.', mk=False),
        ]),
        lesson('en2-3-2', 'Weather & Seasons', '''## Weather
| English | MK |
|---|---|
| sunny | сончев |
| cloudy | облачен |
| rainy | дождлив |
| snowy | снежен |
| windy | ветровит |
| hot | топло |
| cold | студено |

## Seasons
- **spring** — пролет
- **summer** — лето
- **autumn** — есен
- **winter** — зима

### Sentence
- *It`s sunny today.* — Денеска е сончево.
- *In winter it`s cold.* — Во зима е студено.''', [
            mc('e2en-3-2-1', '„Sunny“ е:', ['сончев', 'облачен', 'дождлив', 'снежен'], 'сончев', 'Sun.', 'Сончев.'),
            mc('e2en-3-2-2', '„Summer“ е:', ['пролет', 'лето', 'есен', 'зима'], 'лето', 'Summer.', 'Лето.'),
            mc('e2en-3-2-3', '„Cold“ е:', ['топло', 'студено', 'мокро', 'суво'], 'студено', 'Cold.', 'Студено.'),
            tf('e2en-3-2-4', '„Spring“ значи „пролет“.', 'True', 'Spring.', 'True.', mk=False),
        ]),
        lesson('en2-3-3', 'Places & Nature', '''## Places
| English | MK |
|---|---|
| park | парк |
| zoo | зоолошка градина |
| shop | продавница |
| cinema | кино |
| beach | плажа |
| forest | шума |
| mountain | планина |

## Nature
- **sun** — сонце
- **moon** — месечина
- **star** — ѕвезда
- **tree** — дрво
- **flower** — цвет
- **river** — река
- **sea** — море''', [
            mc('e2en-3-3-1', '„Park“ е:', ['училиште', 'парк', 'кино', 'болница'], 'парк', 'Park.', 'Парк.'),
            mc('e2en-3-3-2', '„Sea“ е:', ['море', 'река', 'планина', 'шума'], 'море', 'Sea.', 'Море.'),
            mc('e2en-3-3-3', '„Forest“ е:', ['Поле', 'Шума', 'Планина', 'Море'], 'Шума', 'Forest.', 'Шума.'),
            tf('e2en-3-3-4', '„Moon“ значи „месечина“.', 'True', 'Moon.', 'True.', mk=False),
        ]),
        lesson('en2-3-test', 'Test — Environment', '## Test: Environment', [
            mc('t2en-3-1', '„Cow“ е:', ['куче', 'мачка', 'крава', 'свиња'], 'крава', 'Cow.', 'Крава.'),
            mc('t2en-3-2', '„Rainy“ е:', ['сончев', 'дождлив', 'снежен', 'облачен'], 'дождлив', 'Rain.', 'Дождлив.'),
            mc('t2en-3-3', '„Tree“ е:', ['цвет', 'дрво', 'трева', 'птица'], 'дрво', 'Tree.', 'Дрво.'),
            tf('t2en-3-4', '„Sun“ значи „сонце“.', 'True', 'Sun.', 'True.', mk=False),
        ], is_test=True),
    ]),

    unit('en2-4', 'Me and Others in Free Time', [
        lesson('en2-4-1', 'Activities', '''## Activities
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
| sleep | спијам |

### „I can / can`t“
- *I can swim.* — Можам да пливам.
- *I can`t fly.* — Не можам да летам.

### „I like / don`t like“
- *I like football.* — Сакам фудбал.''', [
            mc('e2en-4-1-1', '„Read“ е:', ['пиша', 'читам', 'цртам', 'спијам'], 'читам', 'Read.', 'Читам.'),
            mc('e2en-4-1-2', '„I can swim“ значи:', ['Не можам пливам', 'Можам пливам', 'Сакам пливам', 'Мразам пливам'], 'Можам пливам', 'Can.', 'Можам.'),
            mc('e2en-4-1-3', '„Dance“ е:', ['пеам', 'танцувам', 'трчам', 'спијам'], 'танцувам', 'Dance.', 'Танцувам.'),
            tf('e2en-4-1-4', '„I like ____“ значи „Сакам ____“.', 'True', 'Like.', 'True.', mk=False),
        ]),
        lesson('en2-4-2', 'Sports', '''## Sports
| English | MK |
|---|---|
| football | фудбал |
| basketball | кошарка |
| tennis | тенис |
| volleyball | одбојка |
| swimming | пливање |
| running | трчање |
| cycling | возење велосипед |

### Verbs with sports
- **play** with team sports: *play football, play basketball*
- **go** with -ing activities: *go swimming, go running*

### Sentence
- *I play football on Saturday.* — Играм фудбал во сабота.
- *I go swimming every week.* — Пливам секоја недела.''', [
            mc('e2en-4-2-1', '„Football“ е:', ['тенис', 'фудбал', 'кошарка', 'пливање'], 'фудбал', 'Football.', 'Фудбал.'),
            mc('e2en-4-2-2', 'Со спортови со топка користиме:', ['play', 'go', 'do', 'make'], 'play', 'Play football.', 'Play.'),
            mc('e2en-4-2-3', '„Swimming“ е:', ['танцување', 'пливање', 'трчање', 'возење'], 'пливање', 'Swim.', 'Пливање.'),
            tf('e2en-4-2-4', '„Tennis“ значи „тенис“.', 'True', 'Tennis.', 'True.', mk=False),
        ]),
        lesson('en2-4-3', 'Toys & Free Time', '''## Toys
| English | MK |
|---|---|
| ball | топка |
| doll | кукла |
| car | автомобил |
| bike | велосипед |
| teddy bear | плишано меченце |
| puzzle | сложувалка |
| game | игра |

### Sentence
- *I have a red ball.* — Имам црвена топка.
- *Let`s play together!* — Ајде да играме заедно!

### Daily Routine
- *I wake up at 7.* — Будам се во 7.
- *I have lunch at 1.* — Ручам во 1.
- *I go to bed at 9.* — Одам на спиење во 9.''', [
            mc('e2en-4-3-1', '„Ball“ е:', ['кукла', 'топка', 'автомобил', 'велосипед'], 'топка', 'Ball.', 'Топка.'),
            mc('e2en-4-3-2', '„Bike“ е:', ['топка', 'кукла', 'велосипед', 'кутија'], 'велосипед', 'Bike.', 'Велосипед.'),
            mc('e2en-4-3-3', '„I wake up“ значи:', ['Спијам', 'Будам се', 'Јадам', 'Играм'], 'Будам се', 'Wake up.', 'Будам се.'),
            tf('e2en-4-3-4', '„Doll“ значи „кукла“.', 'True', 'Doll.', 'True.', mk=False),
        ]),
        lesson('en2-4-test', 'Test — Free Time', '## Test: Free time', [
            mc('t2en-4-1', '„Dance“ е:', ['пеам', 'танцувам', 'трчам', 'спијам'], 'танцувам', 'Dance.', 'Танцувам.'),
            mc('t2en-4-2', '„I can read“ значи:', ['Не можам читам', 'Можам читам', 'Сакам читам', 'Мразам читам'], 'Можам читам', 'Can.', 'Можам.'),
            mc('t2en-4-3', '„Basketball“ значи:', ['Фудбал', 'Кошарка', 'Тенис', 'Пливање'], 'Кошарка', 'Basket.', 'Кошарка.'),
            tf('t2en-4-4', '„Bike“ е „велосипед“.', 'True', 'Bike.', 'True.', mk=False),
        ], is_test=True),
    ]),
]
