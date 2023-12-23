is_authorized = True

print(is_authorized)
print(type(is_authorized))

# BOOL часто используется при проверке правдивости выражения
print(10 > 56)
print('Yuliia' > 'Yulia')   # посимвольное сравнение
print([1, 2, 3] == [1, 2, 3])

# Конвертация в логическое значение
# bool(my_value)

db_is_available = False
print(db_is_available)
db_is_available = True
print(db_is_available)

print(bool(10))   # T
print(bool('abc'))   # T
print(bool([]))   # F
print(bool([1, 2]))   # T
print(bool(None))   # F
print(bool({'a': 3} == {'a': 5}))   # F
