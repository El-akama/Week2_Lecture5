# 23.10.20 
# множества тип данных такой же как и словарь


# a = set()
# print(type(a))

# a = set('stringstr')
# print(a)

# a = set([1, 2, 1, 2, 3, 'a', 'a', 'b'])
# print(a)

# set - рандомен и удаляет из списка дубликаты? хранятся только уникальные значения, которые неизменяемы

# a = {'a', 'b', 'c'}
# a.add('d')                                # добавляет только один элемент
# a.update({'f', 'l'}, {'m', 'n'})            # добавляет несколько элементов

# print('d' in a)                     # проверка, если элемент во множестве
# print('d' not in a)                     # проверка обратка in

# if 'd' in a:
#     a.remove('d')
# print(a)
 
# a.remove('d')                   # удаляет элемент, если его нет то будет ошибка
# a.discard('d')                      # тоже удаляет, но уже без ошибки, если элемента нет
# a.pop()                             # удаляет рандомно любой элемент и возвращает
# b = a.pop
# print(a)

# l = len(a)                  # считает сколько элементов
# print(l)


# k1 = {'masha', 'sasha', 'nikita', 'syimyk', 'aiperi'}
# k2 = {'syimyk', 'masha', 'adilet'}
# k3 = {'miran', 'dastan', 'nikita'}

# x = dance.intersection(sing)                   # возврат пересекающихся значений

# x = k1.difference(k2, k3)                      # разность относительно чего то

# x = sing.symmetric_difference(dance)           # разность либо - либо, возврат обоих множеств которые нигде не пересекаются

# x = dance.union(sing)                          # объеденяет множества

# x = dance.issuperset(sing)                     # определяет надомножество

# x = sing.issubset(dance)                       # определяет подмножество


# print(dir(dance))

# '-' - разность (.difference)
# '^' - симетричная разность (.symmetric_difference)
# '&' - пересечение (.intersection)
# '|' - объединение (.union)

# x = k1 - k2 - k3
# x = k1 & k2 & k3
# x = k1 ^ k2 ^ k3
# x = k1 | k2 | k3
# print(x)

# frozen_k1 = frozenset(k1)
# # print(type(frozen_k1))
# kk1 = frozenset(k1)
# print(kk1)