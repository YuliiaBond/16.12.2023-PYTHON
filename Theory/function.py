# ФУНКЦИИ

def my_fn(a, b):   # my_fn имя, a, b - параметры
    a = a + 1       # тело функции
    c = a + b
    return c       # возврат результата


my_fn(1, 2)  # вызов функции, 1, 2 - аргументы

# ПРИМЕР 1


def hello():
    print("Hello there!")


hello()

# ПРИМЕР 2


def hello(name):
    print("Hello there,", name)


hello('Yuliia')

# ПРИМЕР 3


def sum_nums(a, b):
    sum = a + b
    # print(sum)
    return sum


first_sum = sum_nums(10, 5)
print(first_sum)

print(sum_nums(sum_nums(1, 3), 6))


# !!! Если нету ключевого слова RETURN, то функция возвращает None