# СПИСОК - упорядоченная последовательность элементов
# Порядок элементов в списке имеет значение
my_fruits = ['apple', 'banana', 'lime']
other_fruits = ['banana', 'apple', 'lime']

posts_ids = [151, 245, 762, 167]
user_inputs = [True, 'hi!', ':)', 10.8]

print(my_fruits == other_fruits)
print(my_fruits[0] == other_fruits[1])
print(user_inputs[-1])

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
# append   добавление новых элементов в конец списка
numbs.append(9)
print(numbs)
# pop  удаление элемента по индексу
numbs.pop()   # удалиться последний элемент
removed_element = numbs.pop(0)
print(removed_element)
print(numbs)
# remove
# numbs.remove(2)
# print(numbs)
# insert
# sort
# index
# clear
# copy
# extend
# reverse
# count
