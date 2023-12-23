# Python - обьектно-ориентированный язык программирования
# Все сущности в Python - обьекты
# Обьект - это экземпляр Класса
# Класс - это шаблон или прототип для создания обьектов
# На основании одного Класса можно создавать много Обьектов
# У каждого Обьекта есть Атрибуты
# Атрибут обьекта называется Методом, если его значение - Функция

# ОСНОВНЫЕ ТИПЫ:
import datetime  # импортирование модуля
str
'Yuliia'   # строка
int
10   # целое число
bool
True
False  # логический
list
[1, 2, 3]   # список
dict
{'min': 5, 'max': 8}  # словарь

# ФУКЦИЯ


def my_fn(a, b):   # my_fn имя, a, b - параметры
    a = a + 1       # тело функции
    c = a + b
    return c       # возврат результата


my_fn(1, 2)  # вызов функции


# ВСТРОЕННЫЕ ФУНКЦИИ
# print()   type()   id()   len()   sum()
# input()   round()   min()   max()   int()
# str()   bool()
# dir() отображает имена всех атрибутов обьекта, их можно вызывать через . (точку)

# name = 'Yuliia'
# print(name.upper())

print(dir(__builtins__))   # вывод всех встроенных функций в пайтане


# ВЫРАЖЕНИЯ (EXPRESSIONS)
# Результатом выражения является Значение:
# 5 + 3   # 8 - сумма значений
# a > b  # True or False
# 'Hello' + 'World'  #  'Hello World'
# my_func(10, 5)   # результат функции


# ИНСТРУКЦИИ (STATEMENTS)
# Инструкция выполняет действие
my_name = 'Yuliia'  # присвоение значения
if my_name:
    print(my_name)  # условная инструкция


# ПЕРЕМЕННЫЕ
# Переменные дают возможность повторного доступа к значениям
# Как называть:
# snake_case - переменные, функции, методы, модули (имя существительное, функция - глагол)
# PascalCase - классы
# my-package - пакеты
# DB_PASSWORD - константы
# Названия переменных должны быть понятными

# В Python существуют изменяемые и нетзменяемые обьекты
# Типы НЕИЗМЕНЯМЫХ обьектов:
# str  int   bool  float  tuple   NoneType  range
# Типы ИЗМЕНЯЕМЫХ обьектов:
# list  dict   set   user-defined classes

# Переменная содержит ссылку на обьект
# Получение адреса обьекта:
print(id(my_name))

# КОНВЕРТАЦИЯ ТИПОВ
# PYTHON не выполняет неявную конвертацию типов значений
# Встроенные функции для явной конвертации типов:
# str()   float()   tuple()
# int()   list()   set()
# ...

# пример 1
# print('10' + 5)   # ошибка
print(5 + int('10'))
print(str(5) + '10')

# пример 2
int_num = 6
float_num = 7.9
# print(int_num + float_num)
print(int_num.__add__(float_num))   # NotImplemented
print(float_num.__radd__(int_num))
str_val = 'abc'
print(int_num * str_val)

# пример 3
bool_val = True
int_val = 7
print(bool_val + int_val)

#  МАГИЧЕСКИЕ МЕТОДЫ - внутренние методы классов и они обычно не вызываются явно
# Например:
# __add__()   __eq__()   __and__()
# __str__()   __neq__()   __or__()
# ...
print(dir(bool))
