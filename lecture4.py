# 22.10.20 
# Лекция - Библиотека

# dictionary = {'key': 'value'}
# словарь - тип данных, который хранит элемент ключи и данные, он может хранить все типы данных и сложные струкутры
# база данных - фильтрация, сортировка, поиск. (алгоритмы)
# hesh для поиска (в библиотеках)

# bishkek = {
#     univery:{
#         gruppy:{
#             studenty:{
#                 primer
#             }
#         }
#     }
# }

# ключами могут быть все неизменяемые типы данных

# student = {
#     'name': 'Bakyt', 
#     'surname': 'Bakytov', 
#     'age': 23, 
#     'languages': ['english', 'russian', 'kyrgyz'],
#     'smokes': False,
#     'other_dict': {1:'one', 2:'two'},
#     True: 'True go',
#     None: 'None go',
#     (1, 2, 3): 'eto tuple'
#     }
# print(student['other_dict'][2])                 # вытаскивать дикты из диктов
# print(student[(1, 2, 3)])

# student = dict(winter = 1, spring = 2, fall = 3)                  # 1 method
# student = dict((('winter', 1), ('spring', 2), ('fall', 3)))         # 2 method

# print(len(student))
# student['name'] = 'Askat'
# print(student['name'])

# del student['name']
# print(student)

# surname = student.get('surname')               # возвращает элемент в ключе (если нету элемента то выдаст None)
# name = student['name']                          # тоже возвращает (но если нету элумента то будет ошибка)
# print(surname)
# print(name)

# my_tuple = (('one', 1), ('two', 2), ('three', 3))
# dict_ = dict(my_tuple)
# print(dict_)

# days = [1, 2, 3]
# day_name = ['mon', 'thus', 'wed']
# dict_days = dict(zip(days, day_name))               # берет списки и делает бибилиотеку
# print(dict_days)                                      # zip соединяет два списка


# методы библиотек

# student = {
#     'name': 'Bakyt', 
#     'surname': 'Bakytov', 
#     'age': 23, 
#     'languages': ['english', 'russian', 'kyrgyz'],
#     'smokes': False,
#     'other_dict': {1:'one', 2:'two'},
#     True: 'True go',
#     None: 'None go',
#     (1, 2, 3): 'eto tuple'
#     }

# student.clear()                   # clear

# new_student = student.copy()      # copy shallow

# s = student.items()               # делает из словаря - кортеж
# s = student.keys()                # список из ключей
# s = student.values()              # возврат значений 

# s = student.pop('name')             # метод поп только надо указывать ключ

# s = student.popitem()                   # по умолчанию возврат посленего итема как кортеж

# s = student.setdefault(10, 'Default')                  # добавляет итемы ключ и значение (по умолчанию ключ, то будет Ноне)

# s = student.update([('black', 6), ('white', 8)])         # добавляет элементы в словарь, один словарь в дргуой словарь
# s = student.update({'key1': 1, 'key2': 2})

# student = dict.fromkeys([1, 2, 3], 'make')          # все итерируемые объекты вначале(без значения по умолчанию будет ноне)
# print(s)

# for item in student.items():
#     print(item)

# print(s)