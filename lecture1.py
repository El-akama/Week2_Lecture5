# name = input("enter your name: ").lower()     # можно так
# print(name)

# name = input("enter your name: ")         # можно и так
# name = name.lower()
# print(name)

# name = input("enter your name: ")     # можно и так
# print(name.lower())

# name = input("enter your name: ")
# name = name.capitalize()                    # делает заглавным только первое слово
# name = name.title()                         # делает заглавным все слова 
# print(name)

# some_string = "Hello World"
# print(some_string.find('l'))            # ищет слева направо
# print(some_string.rfind('l'))           # ищет справа на лево, если нет буквы то пишет -1

# print(some_string.index('o'))              # тоже самое что find, но если нет того символа то выдает ошибку
# print(some_string.rindex('k'))              # тоже что и rfind, но он выдает ошибку если буквы нет

# print(some_string.count('l'))               # считает сколько данных букв

# some_str = input("enter some string: ")
# print(some_str.strip())                     # удаляет лишние пробелы с обеих сторон
# print(some_str.rstrip())                    # удаляет справа пробелы
# print(some_str.lstrip())                    # удаляет слева пробелы
# print(some_str.replace('a', 'o'))           # заменяет одно на другие (1- что заменить, 2- на что заменить )

# print(some_str.split('-'))            # разделяет слова на опрделенный знак

# print(len(some_str.upper().split(' ')))          # можно применять несколько методов

# name = "\telaman \nakama"
# print(name.isalpha())           # смотрит состоит ли строка из букв(только букв)
# print(name.isdigit())           # смотрит только цифры
# print(name.isspace())           # смотрит только на пробелы из спецзнаки(слэши)

# name = input("enter name: ")
# age = 24
# print("hello "+ name + age)   #нельзя
# print("Hello ", name, '. your age', age)      # можно

# print(f'Hello, {name}. Your age is {age}.')         # это форматирование (самая удобная конкатенация, где можно объеденять все)

# print("Hello, {}. Your age is {}.".format(name, age))       # тоже удобно, но надо учитывать окошки ({}), и индексы
