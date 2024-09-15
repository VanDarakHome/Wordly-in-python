from random import choice
game = 0
win_or_not = 0
print("Hello! This is game 'The field of wonders'. If you need to read rules write '1', if not: write '2'")
first_question = input()
while first_question != '1' and first_question != '2':
    print("Please write '1' if you need to read rules, '2' to skip rules")
    first_question = input()
if first_question == '1':
    print("Well, choose the language in which you want to read the rules.")
    print("\n1) Russian")
    print("\n2) English")
    second_question = input()
    while second_question != '1' and second_question != '2':
        print("Please, make a choice!")
        second_question = input()
    if second_question == '1':
        while True:
            print("В данной игре вам необходимо угадать слово, которое зашифровано звёздочками. Пример: ****")
            print("\n1) Далее")
            rule1 = input()
            while rule1 != '1':
                print("Даю вам ещё время, чтобы понять правило игры.")
                rule1 = input()
            print("Для того, чтобы угадать слово мы должны назвать букву. К примеру назовём букву 'а'")
            print("Пример: *а*а")
            print("Как видите, вы угадали букву. Для удобства у вас перед глазами всегда будут буквы, которые вы использовали.")
            print("\n1) Далее")
            rule2 = input()
            while rule2 != '1':
                print("Даю вам ещё время, чтобы понять правило игры.")
                rule2 = input()
            print("Дальше назовём, к примеру, букву 'п'")
            print("Пример: *a*a")
            print("К сожалению, такой буквы нет в этом слове! Тогда назовём букву 'м'")
            print("Пример: мама")
            print("Ура! Вы угадали слово! Начнём игру?")
            print("\n1) Да")
            print("\n2) Повторить правила")
            rule_end = input()
            while rule_end != '1' and rule_end != '2':
                print("Надо что-то выбрать!")
                rule_end = input()
            if rule_end == '1':
                break
            else:
                continue
    else:
        while True:
            print("In this game you need to guess the encrypted word. Example: ****")
            print("\n1) Continue")
            rule1 = input()
            while rule1 != '1':
                print("Ok. Read the rule again and understand it")
                rule1 = input()
            print("To guess this word we have to write a letter. For example, let's enter the letter 'o'")
            print("Example: *oo*")
            print("Nice! We guessed one letter, but it's not all")
            print("\n1) Continue")
            rule2 = input()
            while rule2 != '1':
                print("Ok. Read the rule again and understand it")
                rule2 = input()
            print("Now let's check 'f'. Example: foo*")
            print("Very well! We guessed one more. And it will be easy to guess the last letter. The last letter is 't'")
            print("Example: foot")
            print("Good job. We won that game, but be carefull you may not guess the letter and 'mistakes counter' will increase by 1 unit")
            print("\n1) Let's go to the game")
            print("\n2) Repeat the rules one more time")
            rule_end = input()
            while rule_end != '1' and rule_end != '2':
                print("You need to choose something")
                rule_end = input()
            if rule_end == '1':
                game = 1
                break
            else:
                continue
else:
    print("OK. Good luck!")
    game = 1
print("Now you can change language to Russian")
print("\n1) Change")
print("\n2) Continue with English language")
important_choose = input()
while important_choose != '1' and important_choose != '2':
    print("Please make a choice!")
    important_choose = input()
if important_choose == '1':
    print("Всё прекрасно! Теперь ваша игра будет на Русском языке. Ваши слова тоже будут на Русском языке, если вас это не устраивает,")
    print("даю последний шанс поменять язык")
    print("\n1) Русский язык")
    print("\n2) Английский язык")
    language = input()
    while language != '1' and language != '2':
        print("Определись с выбором языка")
        language = input()
else:
    print("Nice! From this moment, your game will be in English(words will be in English too)")
    print("I give you a last chance to choose your language")
    print("\n1) Russian")
    print("\n2) English")
    language = input()
    while language != '1' and language != '2':
        print("Choose your language!")
        language = input()
print("--------------------------------------------------------------")
print("In the game you can use command !help if you forgot something.")
print("--------------------------------------------------------------")
if language == '1':  # Русский язык
    print("Окей, теперь язык поменять нельзя. Выберите сложность, на которой вы будете играть:")
    print("1) Практика(случайное слово, бесконечное кол-во допустимых ошибок)")
    print("2) Легко(3 - 5 букв в слове, 13 допустимых ошибок)")
    print("3) Средне(6 - 8 букв в слове, 10 допустимых ошибок)")
    print("4) Сложно(9 - 12 букв в слове, 8 допустимых ошибок)")
    print("5) Экстрим(Более 13 букв в слове, 6 допустимых ошибок)")
    BIG_CHOICE = input()
    while BIG_CHOICE != '1' and BIG_CHOICE != '2' and BIG_CHOICE != '3' and BIG_CHOICE != '4' and BIG_CHOICE != '5':
        print("Выбери себе сложность")
        BIG_CHOICE = input()
    if BIG_CHOICE == '1':
        WORDS = ("яма", "нос", "рот", "глаз", "волк", "рыба", "лужа", "краб", "вход", "яйцо", "песок", "силач", "пирог", "сахар",
                 "лимон", "берег", "горка", "тесто", "экран", "замок", "кошка", "штаны", "вечер", "ветер", "ложка", "палка", "книга",
                 "батон", "земля", "масло", "волна", "птица", "пятно", "ведро", "дождь", "шапка", "поиск", "башня", "щипцы", "закат",
                 "пауза", "песня", "сдача", "полка", "билет", "халва", "кочка", "петля", "осень", "ладонь", "король", "опушка", "куртка",
                 "сказка", "звезда", "пряник", "дружба", "секрет", "музыка", "свинья", "камень", "молния", "дерево", "стекло", "минута",
                 "правда", "сердце", "балкон", "стакан", "колесо", "железо", "картон", "грибок", "корова", "остров", "машина", "голова",
                 "радуга", "прятки", "сторож", "защита", "павлин", "рассол", "журнал", "творог", "осадок", "хлопья", "микроб", "письмо",
                 "льдина", "пример", "джокер", "крючок", "пылесос", "полдник", "зеркало", "табурет", "красота", "переход", "желание",
                 "конфета", "учитель", "корабль", "трещина", "мультик", "магазин", "дедушка", "свисток", "игрушка", "доброта", "подушка",
                 "водопад", "загадка", "зарядка", "копейка", "леопард", "ошейник", "водолаз", "батарея", "решётка", "полиция", "стрелка",
                 "бутылка", "записка", "сенокос", "новости", "серебро", "корзина", "овчарка", "айсберг", "пластик", "вторник", "интерес",
                 "лисёнок", "лягушка", "котлета", "накидка", "доспехи", "аквапарк", "снежинка", "пирамида", "кладовка", "картошка",
                 "раковина", "разговор", "прогулка", "сосулька", "картинка", "прихожая", "скатерть", "мармелад", "карамель", "квартира",
                 "непогода", "карточка", "лестница", "переулок", "заставка", "микрофон", "прохожий", "скарабей", "телескоп", "угощение",
                 "пришелец", "доставка", "баклажан", "дикобраз", "барбарис", "работник", "кристалл", "черепаха", "телевизор", "покрывало",
                 "невидимка", "занавеска", "строитель", "бульдозер", "пластилин", "указатель", "градусник", "наволочка", "квитанция",
                 "футболист", "велосипед", "подоконник", "аттракцион", "экскаватор", "троллейбус", "дрессировка", "дельфинарий",
                 "перекрёсток", "тираннозавр", "сигнализация", 'администрация', 'электронейтральный', 'оториноларинголог',
                 'программирование', 'гидроэлектростанция', 'достопримечательность', 'рентгеноэлектрокардиографический',
                 'превысокомногорассмотрительствующий', 'бесконечность', 'умиротворение', 'перпендикуляр', 'электропроводность',
                 'благовоспитанность', 'усовершенствованье')
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        x = list()
        alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
        while word_len != word:
            print("Хотите вывести всё слово сразу? Напишите 123")
            print("\nВы использовали буквы:\n", x)
            print("\nВаше загаданное слово:\n", word_len)
            print("\nВ слове все буквы русские, маленькие(не заглавные)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("-------------------------------------------------------------------")
                print("Вам надо вводить букву каждый раунд пока слово не будет разгадано,")
                print("или ввести всё слово целиком написав 123, однако если вы ошибетесь,")
                print("то игра будет проиграна!")
                print("-------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Введите слово, помните если ошибетесь игра будет проиграна:")
                print("\n1) Назвать слово")
                print("\n2) Я передумал(а)")
                vibor = input()
                while vibor != '1' and vibor != '2':
                    print("Введи 1 или 2")
                    vibot = input()
                if vibor == '1':
                    print("Хорошо введите слово:")
                    nazvanie_word = input()
                    if nazvanie_word != word:
                        win_or_not = 1  # Поражение
                        break
                    else:
                        win_or_not = 0  # Победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("Такой буквы нет в алфавите!")
                answer = input()
            while answer in x:
                print("Вы уже вводили букву", answer)
                answer = input("Введите вашу букву: ")
            x.append(answer)
            if answer in word:
                print("\nПоздравляю!", answer, "есть в слове на этих местах!")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
                mistakes += 1
        if win_or_not == 1:
            print("\nК сожалению вы не угадали слово, вы проиграли!")
        else:
            print("Поздравляю! Вы смогли угадать слово:", word)
            print("Ваше количество ошибок:", mistakes)
    elif BIG_CHOICE == '2':
        print("Напоминаю у вас 13 прав на ошибку")
        WORDS = ("яма", "нос", "рот", "глаз", "волк", "рыба", "лужа", "краб", "вход", "яйцо", "песок", "силач",
                 "пирог", "сахар", "лимон", "берег", "горка", "тесто", "экран", "замок", "кошка", "штаны", "вечер",
                 "ветер", "ложка", "палка", "книга", "батон", "земля", "масло", "волна", "птица", "пятно", "ведро",
                 "дождь", "шапка", "поиск", "башня", "щипцы", "закат", "пауза", "песня", "сдача", "полка", "билет",
                 "халва", "кочка", "петля", "осень")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 13
        x = list()
        alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
        while word_len != word and mistakes < max_mistakes:
            print("Хотите вывести всё слово сразу? Напишите 123")
            print("\nВы использовали буквы:\n", x)
            print("\nВаше загаданное слово:\n", word_len)
            print("\nВ слове все буквы русские, маленькие(не заглавные)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("-------------------------------------------------------------------")
                print("Вам надо вводить букву каждый раунд пока слово не будет разгадано,")
                print("или ввести всё слово целиком написав 123, однако если вы ошибетесь,")
                print("то игра будет проиграна!")
                print("-------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Введите слово, помните если ошибетесь игра будет проиграна:")
                print("\n1) Назвать слово")
                print("\n2) Я передумал(а)")
                vibor = input()
                while vibor != '1' and vibor != '2':
                    print("Введи 1 или 2")
                    vibot = input()
                if vibor == '1':
                    print("Хорошо введите слово:")
                    nazvanie_word = input()
                    if nazvanie_word != word:
                        win_or_not = 1  # Поражение
                        break
                    else:
                        win_or_not = 0  # Победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("Такой буквы нет в алфавите!")
                answer = input()
            while answer in x:
                print("Вы уже вводили букву", answer)
                answer = input("Введите вашу букву: ")
            x.append(answer)
            if answer in word:
                print("\nПоздравляю!", answer, "есть в слове на этих местах!")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Вы проиграли! Слово, которое вам надо было угадать:", word)
        else:
            print("Поздравляю! Вы смогли угадать слово:", word)
            print("Ваше количество ошибок:", mistakes, 'из 13 разрешённых')
    elif BIG_CHOICE == '3':
        print("Напоминаю у вас 10 прав на ошибку")
        WORDS = ("ладонь", "король", "опушка", "куртка", "сказка", "звезда", "пряник", "дружба", "секрет",
                 "музыка", "свинья", "камень", "молния", "дерево", "стекло", "минута", "правда", "сердце",
                 "балкон", "стакан", "колесо", "железо", "картон", "грибок", "корова", "остров", "машина",
                 "голова", "радуга", "прятки", "сторож", "защита", "павлин", "рассол", "журнал", "творог",
                 "осадок", "хлопья", "микроб", "письмо", "льдина", "пример", "джокер", "крючок", "пылесос",
                 "полдник", "зеркало", "табурет", "красота", "переход", "желание", "конфета", "учитель",
                 "корабль", "трещина", "мультик", "магазин", "дедушка", "свисток", "игрушка", "доброта",
                 "подушка", "водопад", "загадка", "зарядка", "копейка", "леопард", "ошейник", "водолаз",
                 "батарея", "решётка", "полиция", "стрелка", "бутылка", "записка", "сенокос", "новости",
                 "серебро", "корзина", "овчарка", "айсберг", "пластик", "вторник", "интерес", "лисёнок",
                 "лягушка", "котлета", "накидка", "доспехи", "аквапарк", "снежинка", "пирамида", "кладовка",
                 "картошка", "раковина", "разговор", "прогулка", "сосулька", "картинка", "прихожая", "скатерть",
                 "мармелад", "карамель", "квартира", "непогода", "карточка", "лестница", "переулок", "заставка",
                 "микрофон", "прохожий", "скарабей", "телескоп", "угощение", "пришелец", "доставка", "баклажан",
                 "дикобраз", "барбарис", "работник", "кристалл", "черепаха")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 10
        x = list()
        alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
        while word_len != word and mistakes < max_mistakes:
            print("Хотите вывести всё слово сразу? Напишите 123")
            print("\nВы использовали буквы:\n", x)
            print("\nВаше загаданное слово:\n", word_len)
            print("\nВ слове все буквы русские, маленькие(не заглавные)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("-------------------------------------------------------------------")
                print("Вам надо вводить букву каждый раунд пока слово не будет разгадано,")
                print("или ввести всё слово целиком написав 123, однако если вы ошибетесь,")
                print("то игра будет проиграна!")
                print("-------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Введите слово, помните если ошибетесь игра будет проиграна:")
                print("\n1) Назвать слово")
                print("\n2) Я передумал(а)")
                vibor = input()
                while vibor != '1' and vibor != '2':
                    print("Введи 1 или 2")
                    vibot = input()
                if vibor == '1':
                    print("Хорошо введите слово:")
                    nazvanie_word = input()
                    if nazvanie_word != word:
                        win_or_not = 1  # Поражение
                        break
                    else:
                        win_or_not = 0  # Победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("Такой буквы нет в алфавите!")
                answer = input()
            while answer in x:
                print("Вы уже вводили букву", answer)
                answer = input("Введите вашу букву: ")
            x.append(answer)
            if answer in word:
                print("\nПоздравляю!", answer, "есть в слове на этих местах!")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Вы проиграли! Слово, которое вам надо было угадать:", word)
        else:
            print("Поздравляю! Вы смогли угадать слово:", word)
            print("Ваше количество ошибок:", mistakes, 'из 10 разрешённых')
    elif BIG_CHOICE == '4':
        print("Напоминаю у вас 8 прав на ошибку")
        WORDS = ("телевизор", "покрывало", "невидимка", "занавеска", "строитель", "бульдозер",
                 "пластилин", "указатель", "градусник", "наволочка", "квитанция", "футболист",
                 "велосипед", "подоконник", "аттракцион", "экскаватор", "троллейбус", "дрессировка",
                 "дельфинарий", "перекрёсток", "тираннозавр", "сигнализация")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 8
        x = list()
        alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
        while word_len != word and mistakes < max_mistakes:
            print("Хотите вывести всё слово сразу? Напишите 123")
            print("\nВы использовали буквы:\n", x)
            print("\nВаше загаданное слово:\n", word_len)
            print("\nВ слове все буквы русские, маленькие(не заглавные)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("-------------------------------------------------------------------")
                print("Вам надо вводить букву каждый раунд пока слово не будет разгадано,")
                print("или ввести всё слово целиком написав 123, однако если вы ошибетесь,")
                print("то игра будет проиграна!")
                print("-------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Введите слово, помните если ошибетесь игра будет проиграна:")
                print("\n1) Назвать слово")
                print("\n2) Я передумал(а)")
                vibor = input()
                while vibor != '1' and vibor != '2':
                    print("Введи 1 или 2")
                    vibot = input()
                if vibor == '1':
                    print("Хорошо введите слово:")
                    nazvanie_word = input()
                    if nazvanie_word != word:
                        win_or_not = 1  # Поражение
                        break
                    else:
                        win_or_not = 0  # Победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("Такой буквы нет в алфавите!")
                answer = input()
            while answer in x:
                print("Вы уже вводили букву", answer)
                answer = input("Введите вашу букву: ")
            x.append(answer)
            if answer in word:
                print("\nПоздравляю!", answer, "есть в слове на этих местах!")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Вы проиграли! Слово, которое вам надо было угадать:", word)
        else:
            print("Поздравляю! Вы смогли угадать слово:", word)
            print("Ваше количество ошибок:", mistakes, 'из 8 разрешённых')
    else:
        print("Напоминаю у вас 6 прав на ошибку")
        WORDS = ('администрация', 'электронейтральный', 'оториноларинголог', 'программирование',
                 'гидроэлектростанция', 'достопримечательность', 'рентгеноэлектрокардиографический',
                 'превысокомногорассмотрительствующий', 'бесконечность', 'умиротворение',
                 'перпендикуляр', 'электропроводность', 'благовоспитанность', 'усовершенствованье')
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 6
        x = list()
        alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',]
        while word_len != word and mistakes < max_mistakes:
            print("Хотите вывести всё слово сразу? Напишите 123")
            print("\nВы использовали буквы:\n", x)
            print("\nВаше загаданное слово:\n", word_len)
            print("\nВ слове все буквы русские, маленькие(не заглавные)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("-------------------------------------------------------------------")
                print("Вам надо вводить букву каждый раунд пока слово не будет разгадано,")
                print("или ввести всё слово целиком написав 123, однако если вы ошибетесь,")
                print("то игра будет проиграна!")
                print("-------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Введите слово, помните если ошибетесь игра будет проиграна:")
                print("\n1) Назвать слово")
                print("\n2) Я передумал(а)")
                vibor = input()
                while vibor != '1' and vibor != '2':
                    print("Введи 1 или 2")
                    vibot = input()
                if vibor == '1':
                    print("Хорошо введите слово:")
                    nazvanie_word = input()
                    if nazvanie_word != word:
                        win_or_not = 1  # Поражение
                        break
                    else:
                        win_or_not = 0  # Победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("Такой буквы нет в алфавите!")
                answer = input()
            while answer in x:
                print("Вы уже вводили букву", answer)
                answer = input("Введите вашу букву: ")
            x.append(answer)
            if answer in word:
                print("\nПоздравляю!", answer, "есть в слове на этих местах!")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nИзвините, буквы \"" + answer + "\" нет в слове.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Вы проиграли! Слово, которое вам надо было угадать:", word)
        else:
            print("Поздравляю! Вы смогли угадать слово:", word)
            print("Ваше количество ошибок:", mistakes, 'из 6 разрешённых')
else:
    print("Ok. Now you need to choose your game difficulty:")
    print("\n1)Practice(you have infinity attempts, the word is random)")
    print("2) Easy(you have only 13 attempts to guess the word, there are 3 to 5 characters in a word)")
    print("3) Normal(you have only 10 attempts to guess the word, there are 6 to 8 characters in a word)")
    print("4) Hard(you have only 8 attempts to guess the word, there are 9 to 12 characters in a word)")
    BIG_CHOICE = input()
    while BIG_CHOICE != '1' and BIG_CHOICE != '2' and BIG_CHOICE != '3' and BIG_CHOICE != '4':
        print("Please choose your game difficulty")
        BIG_CHOICE = input()
    if BIG_CHOICE == '1':
        WORDS = ("fox", "egg", "dog", "cat", "foot", "hand", "head", "nose", "card", "lane", "news",
                 "song", "frog", "cape", "bike", "hook", "wave", "mouse", "noise", "diver", "tower",
                 "arrow", "pause", "treat", "alien", "shelf", "joker", "armor", "halva", "staff", "puppy",
                 "search", "collar", "police", "bottle", "ladder", "sunset", "silver", "basket", "change",
                 "flakes", "letter", "ticket", "worker", "hummer", "turtle", "autumn", "galaxy", "matrix",
                 "subway", "zodiac", "zombie", "joking", "rainbow", "leopard", "caramel", "battery",
                 "peacock", "receipt", "microbe", "iceberg", "plastic", "tuesday", "example", "crystal",
                 "unknown", "jackpot", "watchman", "training", "entrance", "magazine", "shepherd",
                 "delivery", "interest", "football", "marmalade", "apartment", "telescope", "excavator",
                 "attraction", "protection", "crossroads", "pillowcase", "microphone", "trolleybus",
                 "transcript", "thermometer", "screensaver", "tyrannosaur", "dolphinarium")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        x = list()
        alphavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while word_len != word:
            print("If you want know the word write 123")
            print("\nYou used letters:\n", x)
            print("\nYour hidden word:\n", word_len)
            print("\nAll letters in the word are English, small(not capital letters)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("--------------------------------------------------------------------------")
                print("Every round you need to guess and enter the letter in the hidden word,")
                print("or enter the word(write 123), but be carefull if you don't guess the word,")
                print("game will be lost!")
                print("--------------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Ok, if you don't guess the word now, you lose this game.")
                print("\n1) Ok i agree")
                print("\n2) No, I'm not sure")
                vibor2 = input()
                while vibor2 != '1' and vibor2 != '2':
                    print("Please make a choice!")
                    vibor2 = input()
                if vibor2 == '1':
                    print("Ok enter the word:")
                    final_vibor = input()
                    if final_vibor != word:
                        win_or_not = 1  # поражение
                        break
                    else:
                        win_or_not = 0  # победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("There is no such letter in the alphabet!")
                answer = input()
            while answer in x:
                print("You have already entered the letter", answer)
                answer = input("Enter your letter: ")
            x.append(answer)
            if answer in word:
                print("\nCongratulations!", answer, "there is in this word.")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nSorry, letter \"" + answer + "\" not in the word.")
                mistakes += 1
        if win_or_not == 1:
            print("You lose! Correct word was:", word)
        else:
            print("Congratulations! Were you able to guess the word:", word)
            print("Your number of errors:", mistakes)
    elif BIG_CHOICE == '2':
        print("You have 13 attempts to guess the word")
        WORDS = ("fox", "egg", "dog", "cat", "foot", "hand", "head", "nose", "card", "lane", "news",
                 "song", "frog", "cape", "bike", "hook", "wave", "mouse", "noise", "diver", "tower",
                 "arrow", "pause", "treat", "alien", "shelf", "joker", "armor", "halva", "staff", "puppy")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 13
        x = list()
        alphavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while word_len != word and max_mistakes > mistakes:
            print("If you want know the word write 123")
            print("\nYou used letters:\n", x)
            print("\nYour hidden word:\n", word_len)
            print("\nAll letters in the word are English, small(not capital letters)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("--------------------------------------------------------------------------")
                print("Every round you need to guess and enter the letter in the hidden word,")
                print("or enter the word(write 123), but be carefull if you don't guess the word,")
                print("game will be lost!")
                print("--------------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Ok, if you don't guess the word now, you lose this game.")
                print("\n1) Ok i agree")
                print("\n2) No, I'm not sure")
                vibor2 = input()
                while vibor2 != '1' and vibor2 != '2':
                    print("Please make a choice!")
                    vibor2 = input()
                if vibor2 == '1':
                    print("Ok enter the word:")
                    final_vibor = input()
                    if final_vibor != word:
                        win_or_not = 1  # поражение
                        break
                    else:
                        win_or_not = 0  # победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("There is no such letter in the alphabet!")
                answer = input()
            while answer in x:
                print("You have already entered the letter", answer)
                answer = input("Enter your letter: ")
            x.append(answer)
            if answer in word:
                print("\nCongratulations!", answer, "there is in this word.")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nSorry, letter \"" + answer + "\" not in the word.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Sorry, you lose. Correct word was:", word)
        else:
            print("Congratulations! Were you able to guess the word:", word)
            print("Your number of errors:", mistakes, 'out of 13 possible.')
    elif BIG_CHOICE == '3':
        print("You have 10 attempts to guess the word")
        WORDS = ("search", "collar", "police", "bottle", "ladder", "sunset",
                 "silver", "basket", "change", "flakes", "letter", "ticket",
                 "worker", "hummer", "turtle", "autumn", "galaxy", "matrix",
                 "subway", "zodiac", "zombie", "joking", "rainbow", "leopard",
                 "caramel", "battery", "peacock", "receipt", "microbe", "iceberg",
                 "plastic", "tuesday", "example", "crystal", "unknown", "jackpot",
                 "watchman", "training", "entrance", "magazine", "shepherd",
                 "delivery", "interest", "football")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 10
        x = list()
        alphavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while word_len != word and max_mistakes > mistakes:
            print("If you want know the word write 123")
            print("\nYou used letters:\n", x)
            print("\nYour hidden word:\n", word_len)
            print("\nAll letters in the word are English, small(not capital letters)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("--------------------------------------------------------------------------")
                print("Every round you need to guess and enter the letter in the hidden word,")
                print("or enter the word(write 123), but be carefull if you don't guess the word,")
                print("game will be lost!")
                print("--------------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Ok, if you don't guess the word now, you lose this game.")
                print("\n1) Ok i agree")
                print("\n2) No, I'm not sure")
                vibor2 = input()
                while vibor2 != '1' and vibor2 != '2':
                    print("Please make a choice!")
                    vibor2 = input()
                if vibor2 == '1':
                    print("Ok enter the word:")
                    final_vibor = input()
                    if final_vibor != word:
                        win_or_not = 1  # поражение
                        break
                    else:
                        win_or_not = 0  # победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("There is no such letter in the alphabet!")
                answer = input()
            while answer in x:
                print("You have already entered the letter", answer)
                answer = input("Enter your letter: ")
            x.append(answer)
            if answer in word:
                print("\nCongratulations!", answer, "there is in this word.")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nSorry, letter \"" + answer + "\" not in the word.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Sorry, you lose. Correct word was:", word)
        else:
            print("Congratulations! Were you able to guess the word:", word)
            print("Your number of errors:", mistakes, 'out of 10 possible.')
    else:
        print("You have 8 attempts to guess the word")
        WORDS = ("marmalade", "apartment", "telescope", "excavator",
                 "attraction", "protection", "crossroads", "pillowcase",
                 "microphone", "trolleybus", "transcript", "thermometer",
                 "screensaver", "tyrannosaur", "dolphinarium")
        word = choice(WORDS)
        word_len = "*" * len(word)
        mistakes = 0
        max_mistakes = 8
        x = list()
        alphavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while word_len != word and max_mistakes > mistakes:
            print("If you want know the word write 123")
            print("\nYou used letters:\n", x)
            print("\nYour hidden word:\n", word_len)
            print("\nAll letters in the word are English, small(not capital letters)")
            print('-----------------------------------------------')
            answer = input()
            if answer == '!help':
                print("--------------------------------------------------------------------------")
                print("Every round you need to guess and enter the letter in the hidden word,")
                print("or enter the word(write 123), but be carefull if you don't guess the word,")
                print("game will be lost!")
                print("--------------------------------------------------------------------------")
                continue
            if answer == '123':
                print("Ok, if you don't guess the word now, you lose this game.")
                print("\n1) Ok i agree")
                print("\n2) No, I'm not sure")
                vibor2 = input()
                while vibor2 != '1' and vibor2 != '2':
                    print("Please make a choice!")
                    vibor2 = input()
                if vibor2 == '1':
                    print("Ok enter the word:")
                    final_vibor = input()
                    if final_vibor != word:
                        win_or_not = 1  # поражение
                        break
                    else:
                        win_or_not = 0  # победа
                        break
                else:
                    continue
            while answer not in alphavit:
                print("There is no such letter in the alphabet!")
                answer = input()
            while answer in x:
                print("You have already entered the letter", answer)
                answer = input("Enter your letter: ")
            x.append(answer)
            if answer in word:
                print("\nCongratulations!", answer, "there is in this word.")
                new = ""
                for i in range(len(word)):
                    if answer == word[i]:
                        new += answer
                    else:
                        new += word_len[i]
                word_len = new
            else:
                print("\nSorry, letter \"" + answer + "\" not in the word.")
                mistakes += 1
        if mistakes == max_mistakes or win_or_not == 1:
            print("Sorry, you lose. Correct word was:", word)
        else:
            print("Congratulations! Were you able to guess the word:", word)
            print("Your number of errors:", mistakes, 'out of 8 possible.')
