# СПИСОК - упорядоченная последовательность элементов
# Порядок элементов в списке имеет значение
my_fruits = ['apple', 'banana', 'lime']
other_fruits = ['banana', 'apple', 'lime']

posts_ids = [151, 245, 762, 167]
user_inputs = [True, 'hi!', ':)', 10.8]

print(my_fruits == other_fruits)
print(my_fruits[0] == other_fruits[1])
print(user_inputs[-1])

print(dir(my_fruits))   # посмотреть методы списка

print(len(posts_ids))   # длина списка

print(user_inputs)
user_inputs[1] = 'hello!'   # изменяем список
print(user_inputs)
del user_inputs[-1]   # удаляем элемент
print(user_inputs)

users = [{'user_id': 123, 'user_name': 'Alica'},
         {'user_id': 345, 'user_name': 'Bob'}]
print(len(users))
print(users[1]['user_name'])

fruit1 = 'banana'
fruit2 = 'apple'
fruit3 = 'lime'
all_fruits = [fruit1, fruit2, fruit3]   # создание списка через переменные
print(all_fruits)


# МЕТОДЫ СПИСКОВ обьекты наследуют от класса List
numbs = [1, 3, 5, 7]
print(numbs)
# append   добавление новых элементов в конец списка (изменяет)
numbs.append(9)
print(numbs)
# pop  удаление элемента по индексу (изменяет)
numbs.pop()   # удалиться последний элемент
removed_element = numbs.pop(0)   # удалит по индексу
print(removed_element)
print(numbs)
# remove
# numbs.remove(2)
# print(numbs)
# insert   вставляет обьект перед указанным индексом
my_nums = [10, 50, 0, 5, 100]
my_nums.insert(2, -7)
print(my_nums)
# sort   сортировка элементов по порядку возрастания (изменяет)
posts_ids = [245, 151, 765, 178]
posts_ids.sort()
print(posts_ids)
posts_ids.sort(reverse=True)  # сортировка по убыванмю
print(posts_ids)
# index
# clear   очищает список
my_nums = [10, 50, 0, 5, 100]
my_nums.clear()
print(my_nums)
# copy  копируем список, не изменяет
my_nums = [10, 50, 0, 5, 100]
other_nums = my_nums.copy()
print(id(my_nums))
print(id(other_nums))
# extend   расширить список, добавляя элементы другой последовательности
my_nums = [10, 50, 0, 5, 100]
my_nums.extend('abc')
print(my_nums)
# reverse
# count   сколько раз в списке повторяется элемент
my_nums = [10, 50, 0, 5, 5, 100]
res = my_nums.count(5)
print(res)


# КОНВЕРТАЦИЯ В СПИСКАХ

greeting = "Hello from Python"   # строка в список
greeting_letters = list(greeting)
print(greeting_letters)

# словарь в список, получаем только ключи, значения исчежают
my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)
print(my_dict_keys)


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ В СПИСКАХ

rating = [2.5, 6.0, 5.9, 4.2]
print(min(rating))
print(max(rating))
print(sum(rating))
print(sum(rating)/len(rating))


# ОБЬЕДИНЕНИЕ СПИСКОВ

my_ratings = [2.5, 5.0]
other_ratings = [7.8, 4.2, 1.8]
all_ratings = my_ratings + other_ratings
print(all_ratings)

# НАРЕЗКА СПИСКОВ

ratings = [2.5, 6.0, 5.9, 4.2]
first_two_ratings = ratings[:2]
print(first_two_ratings)
middle_ratings = ratings[1:-1]
print(middle_ratings)
last_two_ratings = ratings[-2:]
print(last_two_ratings)


# КОПИРОВАНИЕ СПИСКОВ

my_cars = ['BMW', 'Mercedes']
copied_cars = my_cars   # ссылаются на одно место в памяти
copied_cars.append('Audi')
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars))

# копирование в новый список, вариант 1
my_cars2 = ['BMW', 'Mercedes']
# создаем новый список, а не копируем (использую slice)
copied_cars2 = my_cars2[:]
copied_cars2.append('Audi')
print(copied_cars2)
print(my_cars2)
print(id(my_cars2) == id(copied_cars2))

# копирование в новый список, вариант 2
my_cars3 = ['BMW', 'Mercedes']
# создаем новый список через метод copy
copied_cars3 = my_cars3.copy()
copied_cars3.append('Audi')
print(copied_cars3)
print(my_cars3)
print(id(my_cars3) == id(copied_cars3))

# копирование в новый список, вариант 3
my_cars4 = ['BMW', 'Mercedes']
# создаем новый список через встроенную функцию list
copied_cars4 = list(my_cars4)
copied_cars4.append('Audi')
print(copied_cars4)
print(my_cars4)
print(id(my_cars4) == id(copied_cars4))
