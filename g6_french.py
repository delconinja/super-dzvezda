# -*- coding: utf-8 -*-
"""Grade 6 French — BRO 1:1: 3 теми / 7 lessons + 3 tests."""

FRENCH = [

unit('fr6-1', 'Premiers contacts — Први контакти', [
    lesson('fr6-1-1', 'Bonjour! Поздравување и претставување', '''## Поздрави

| French | MK |
|---|---|
| Bonjour! | Добар ден! |
| Bonsoir! | Добра вечер! |
| Salut! | Здраво/Чао! |
| Au revoir! | Довидување! |
| Bonne nuit! | Добра ноќ! |
| Merci! | Благодарам! |
| S`il vous plaît | Ве молам |
| Pardon | Извини / простете |

## Претставување

- *Comment t`appelles-tu?* — Како се викаш?
- *Je m`appelle Marie.* — Се викам Мари.
- *Quel âge as-tu?* — Колку години имаш?
- *J`ai douze ans.* — Имам 12 години.
- *D`où viens-tu?* — Од каде си?
- *Je viens de Macédoine.* — Од Македонија сум.
- *Où habites-tu?* — Каде живееш?
- *J`habite à Skopje.* — Живеам во Скопје.

## Алфабет и фонетика

Францускиот има 26 букви + специјални акценти:
- **é** (акцент акут): café
- **è** (акцент грав): père
- **ê** (циркумфлекс): forêt
- **ç** (седила): garçon
- **ô, î, û** — различни акценти

### Особени звуци
- **u** ~ германско „ü“
- **r** — гарлено, грлено
- Многу букви не се читаат на крајот на зборот!

### Броеви 1-10
un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix''', [
        mc('ef6-1-1-1', 'Како се вели „Добар ден“ на француски?', ['Bonsoir', 'Bonjour', 'Au revoir', 'Salut'], 'Bonjour', 'Bon + jour.', 'Bonjour = добар ден.'),
        mc('ef6-1-1-2', '„Je m`appelle Anna“ значи:', ['Здраво Ана', 'Се викам Ана', 'Имам Ана', 'Од Ана сум'], 'Се викам Ана', 's`appeler = се вика.', 'Je m`appelle = Се викам.'),
        mc('ef6-1-1-3', 'Бројот 5 на француски е:', ['quatre', 'cinq', 'six', 'sept'], 'cinq', '5 = cinq.', 'Cinq = 5.'),
        tf('ef6-1-1-4', 'На француски „merci“ значи „благодарам“.', 'Точно', 'Универзално познат збор.', 'Точно — merci = благодарам.'),
    ]),
    lesson('fr6-1-2', 'Famille et goûts — Семејство и интереси', '''## Семејство (la famille)

| French | MK |
|---|---|
| la mère / maman | мајка |
| le père / papa | татко |
| la sœur | сестра |
| le frère | брат |
| la grand-mère | баба |
| le grand-père | дедо |
| l`oncle | вујко/стрико |
| la tante | тетка/стрина |
| le cousin / la cousine | братучед/братучетка |

### Членови (артикли)
- **le** — машки определен (le père)
- **la** — женски определен (la mère)
- **les** — множина (les parents)
- **un** — машки неопределен (un livre)
- **une** — женски неопределен (une fille)

### Глаголот être (да биде)
| Лице | Форма |
|---|---|
| je | suis |
| tu | es |
| il/elle | est |
| nous | sommes |
| vous | êtes |
| ils/elles | sont |

## Што сакаш — goûts (вкусови)

- *Qu`est-ce que tu aimes faire?* — Што сакаш да правиш?
- *J`aime lire.* — Сакам да читам.
- *J`aime jouer au football.* — Сакам да играм фудбал.
- *J`aime danser.* — Сакам да танцувам.
- *Je n`aime pas les légumes.* — Не сакам зеленчук.

### Хобија
le sport, la musique, la lecture, la danse, le cinéma, les jeux vidéo''', [
        mc('ef6-1-2-1', '„mère“ значи:', ['татко', 'мајка', 'сестра', 'брат'], 'мајка', 'la mère.', 'Mère = мајка.'),
        mc('ef6-1-2-2', 'Член на „père“ е:', ['la', 'le', 'les', 'une'], 'le', 'Машки определен.', 'Le père = машки определен.'),
        mc('ef6-1-2-3', '„J`ai 12 ans“ значи:', ['Сакам 12', 'Имам 12 години', '12 е мое', 'На 12 сум'], 'Имам 12 години', 'avoir = има, ans = години.', 'J`ai ... ans = имам ... години.'),
        mc('ef6-1-2-4', 'Како велиш „Сакам да читам“?', ['Je joue lire', 'J`aime lire', 'Je suis lire', 'Je danse lire'], 'J`aime lire', 'aimer = сака.', 'J`aime lire = сакам да читам.'),
    ]),
    lesson('fr6-1-test', 'Test — Premiers contacts', '## Тест: Premiers contacts', [
        mc('tf6-1-1', '„Au revoir“ значи:', ['Здраво', 'Довидување', 'Благодарам', 'Ве молам'], 'Довидување', 'При разделба.', 'Au revoir = довидување.'),
        mc('tf6-1-2', 'Член на „sœur“ е:', ['le', 'la', 'les', 'un'], 'la', 'Женски.', 'La sœur — женски определен.'),
        mc('tf6-1-3', 'Бројот 8 на француски:', ['sept', 'huit', 'neuf', 'dix'], 'huit', '8 = huit.', 'Huit = 8.'),
        mc('tf6-1-4', 'Како велиш „Од Македонија сум“?', ['Je m`appelle Macédoine', 'Je viens de Macédoine', 'J`ai Macédoine', 'Je suis Macédoine'], 'Je viens de Macédoine', 'venir de = доаѓа од.', 'Je viens de Macédoine = доаѓам од Македонија.'),
    ], is_test=True),
]),

unit('fr6-2', 'L`école — Училиштето', [
    lesson('fr6-2-1', 'Les matières, les jours et l`heure', '''## Училиште (l`école)

### Школски прибор
- le stylo — пенкало
- le crayon — молив
- le cahier — тетратка
- le livre — книга
- la trousse — пенал
- le sac (à dos) — ранец

### Предмети (les matières)
- les mathématiques — математика
- le français — француски
- l`anglais — англиски
- l`histoire — историја
- la géographie — географија
- la biologie — биологија
- le sport — спорт
- la musique — музика
- l`art — уметност

### Дни на неделата (les jours)
lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche

### Времето (l`heure)
- *Quelle heure est-il?* — Колку е часот?
- *Il est huit heures.* — Часот е 8.
- *Il est huit heures et demie.* — 8:30.
- *Il est neuf heures moins le quart.* — 8:45 (без четвртина до 9).
- *Il est neuf heures et quart.* — 9:15.

### Часови
- *J`ai français lundi.* — Имам француски во понеделник.
- *Le cours commence à 8 heures.* — Часот почнува во 8.''', [
        mc('ef6-2-1-1', '„livre“ значи:', ['пенал', 'тетратка', 'книга', 'молив'], 'книга', 'le livre.', 'Livre = книга.'),
        mc('ef6-2-1-2', 'Кој ден е „mercredi“?', ['Понеделник', 'Вторник', 'Среда', 'Четврток'], 'Среда', 'Среден ден.', 'Mercredi = среда.'),
        mc('ef6-2-1-3', '„Il est huit heures et demie“ значи:', ['8:00', '8:30', '8:15', '8:45'], '8:30', 'demie = половина.', 'Et demie = и половина → 8:30.'),
        mc('ef6-2-1-4', 'Како велиш „Имам математика“?', ['J`ai mathématiques', 'Je suis mathématiques', 'Je m`appelle mathématiques', 'J`aime mathématiques'], 'J`ai mathématiques', 'avoir = има.', 'J`ai mathématiques = имам математика.'),
    ]),
    lesson('fr6-2-test', 'Test — L`école', '## Тест: L`école', [
        mc('tf6-2-1', '„dimanche“ е:', ['Сабота', 'Недела', 'Понеделник', 'Петок'], 'Недела', 'Ден на Господа.', 'Dimanche = недела.'),
        mc('tf6-2-2', '„Quelle heure est-il?“ значи:', ['Колку години имаш?', 'Колку е часот?', 'Што сакаш?', 'Од каде си?'], 'Колку е часот?', 'heure = час.', 'Quelle heure est-il = колку е часот.'),
        mc('tf6-2-3', 'Бројот 6 на француски:', ['cinq', 'six', 'sept', 'huit'], 'six', '6 = six.', 'Six = 6.'),
        tf('tf6-2-4', '„Le sport“ е машки определен член.', 'Точно', 'le = машки.', 'Точно — le sport — машки определен член.'),
    ], is_test=True),
]),

unit('fr6-3', 'Le temps libre — Слободно време', [
    lesson('fr6-3-1', 'Les activités et les goûts', '''## Активности во слободно време

- jouer au football — играње фудбал
- jouer au basket — играње кошарка
- nager — плива
- danser — танцува
- chanter — пее
- lire — чита
- écouter de la musique — слуша музика
- regarder la télé — гледа телевизија
- faire du sport — спортува
- faire du vélo — вози велосипед

### Глаголот jouer (игра)
| Лице | Форма |
|---|---|
| je | joue |
| tu | joues |
| il/elle | joue |
| nous | jouons |
| vous | jouez |
| ils/elles | jouent |

(Сите крајови -e/-es се читаат еднакво — нем!)

### „aimer + infinitive“
- *J`aime danser.* — Сакам да танцувам.
- *Tu aimes chanter?* — Сакаш да пееш?
- *Il aime jouer au foot.* — Тој сака да игра фудбал.

### Изразување интензитет
- *J`adore le sport!* — Обожавам спорт!
- *J`aime beaucoup la musique.* — Многу ја сакам музиката.
- *J`aime bien les films.* — Сакам филмови.
- *Je n`aime pas...* — Не сакам...
- *Je déteste...* — Мразам...''', [
        mc('ef6-3-1-1', '„nager“ значи:', ['танцува', 'пее', 'плива', 'трча'], 'плива', 'nager = плива.', 'Nager = плива.'),
        mc('ef6-3-1-2', 'Како велиш „Сакам да читам“?', ['Je danse lire', 'J`aime lire', 'Je joue lire', 'J`adore football'], 'J`aime lire', 'aimer + infinitive.', 'J`aime + infinitive = сакам да...'),
        mc('ef6-3-1-3', '„regarder la télé“ значи:', ['слуша радио', 'гледа ТВ', 'игра ТВ', 'купува ТВ'], 'гледа ТВ', 'regarder = гледа.', 'Regarder = гледа; la télé = телевизија.'),
        mc('ef6-3-1-4', '„J`adore le sport“ е:', ['Не сакам спорт', 'Сакам спорт', 'Обожавам спорт', 'Мразам спорт'], 'Обожавам спорт', 'adorer = обожава.', 'J`adore = обожавам (поголем интензитет од сакам).'),
    ]),
    lesson('fr6-3-test', 'Test — Le temps libre', '## Тест: Le temps libre', [
        mc('tf6-3-1', '„chanter“ значи:', ['танцува', 'пее', 'игра', 'спие'], 'пее', 'Chant = пеење.', 'Chanter = пее.'),
        mc('tf6-3-2', '„Je déteste les légumes“ значи:', ['Сакам зеленчук', 'Мразам зеленчук', 'Купувам зеленчук', 'Готвам зеленчук'], 'Мразам зеленчук', 'détester = мрази.', 'Je déteste = мразам.'),
        mc('tf6-3-3', '„faire du vélo“ значи:', ['танцува', 'плива', 'вози велосипед', 'спортува'], 'вози велосипед', 'vélo = велосипед.', 'Faire du vélo = возење велосипед.'),
        tf('tf6-3-4', 'Францускиот често не ги чита крајовите на глаголските форми.', 'Точно', 'Тихи букви.', 'Точно — многу букви на крај од зборови не се читаат (нем).'),
    ], is_test=True),
]),

]
