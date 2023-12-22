num = 10

print(type(num))

# any_num = input("Enter any number: ")
# # или
# # any_num = int(input("Enter any number: "))
# print(any_num)
# print(type(any_num))   # STR
# any_num2 = int(any_num)
# print(type(any_num2))  # INT

# ВОЗВЕДЕНИЕ В СТЕПЕНЬ
base = 5
power = 3
result = pow(base, power)  # 125
print(type(result))

# ЧИСЛА С ДЕСЯТИЧНОЙ ТОЧКОЙ

average_price = 17.25
print(average_price)
print(type(average_price))

print(int(average_price))

str_temperature = '14.5'
temperature = float(str_temperature)
print(temperature)
print(type(temperature))

# ОКРУГЛЕНИЕ ЧИСЕЛ

rate = 18.08
print(round(rate))
print(type(rate))
print(type(round(rate)))

# КОМПЛЕКСНЫЕ ЧИСЛА
# Комплексное число состоит из действительной и мнимой частей

complex_a = 3 + 5j
complex_b = 4 + 7j

sum = complex_a + complex_b   # + - * /
print(sum)
print(type(sum))
