# СЛОВАРЬ - набор элементов ключ:значение
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
print(my_motorbike == other_motorbike)
print(id(my_motorbike) == id(other_motorbike))

# Удаление элементов
# видео 55
