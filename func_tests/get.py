# Функция get(list, index, default = None) извлекает из списка значение по
# указанному индексу, если индекс существует. Если индекс не существует, возвращает значение по умолчанию.
# Функция работает только с неотрицательными индексами:


def get(coll, index, default=None):
    if index >= len(coll) or index < 0:
        if default is not None:
            return default
        return None

    return coll[index]

# numbers = [1, 2, 3, 4]
# get(numbers, 1)  # 2
# print(get(numbers, 5, 'nothing'))# 'nothing'
# print(get(numbers, 3))
# print(get(numbers, -5, 'bhg'))

#
# def get(coll, index, default=None):
#     if index >= len(coll) or index < 0:
#         return None
#
#     if default is not None:
#         return default
#
#     else:
#         return coll[index]
#
#
# numbers = [1, 2, 3, 4]
# get(numbers, 1)  # 2
# print(get(numbers, 3, 'nothing'))  # 'nothing'
# print(get(numbers, 5))
# print(get(numbers, -5, 'bhg'))