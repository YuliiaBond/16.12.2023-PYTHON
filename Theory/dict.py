# СЛОВАРЬ - набор элементов (ключ:значение)
# Порядок элементов в словаре НЕ имеет значения (индексов нет)
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}
other_motorbike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati',
}
print(my_motorbike)
print(other_motorbike)
print(my_motorbike == other_motorbike)   # технически одинаковые словари
print(id(my_motorbike) == id(other_motorbike))   # разные обьекты

# Получение значения в []
print(my_motorbike['brand'])

# Изменение значений
my_motorbike['price'] = 2000
print(my_motorbike['price'])

# Добавление новых элементов
my_motorbike['is_new'] = True
print(my_motorbike)

# Удаление элементов
del my_motorbike['engine_vol']
print(my_motorbike)

# Доступ к значению элемента с помощью переменной
my_bike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}
key_name = 'brand'
my_bike[key_name] = 'BMW'
print(my_bike)

# Вложенные словари
my_motorbike2 = {
    'brand': 'Ducati',
    'price_info': {
        'price': 10000,
        'is_available': True},
    'engine_vol': 1.2,
}
print(my_motorbike2['price_info']['price'])
