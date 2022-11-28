#
# Функция `my_slice(list, begin, end)` возвращает новый список, содержащий копию части исходного списка.
#
# Аргументы:
#
# - `list` - исходный список.
# - `begin` - индекс, по которому начинается извлечение. Если индекс отрицательный, `begin` указывает
# смещение от конца списка. По умолчанию равен нулю.
# - `end` - индекс, по которому заканчивается извлечение (не включая элемент с индексом `end`). Если индекс
# отрицательный, `end` указывает смещение от конца списка. По умолчанию равен длине исходного списка.
#

def my_slice(coll, start=0, end=None):
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return []

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]

# numbers = [1, 2, 3, 4, 5]
# my_slice(numbers)  # [1, 2, 3, 4, 5]
# my_slice(numbers, 1, 4)  # [2, 3, 4]
# my_slice(numbers, -4, -2)  # [2, 3]
# my_slice(numbers, 7)  # []
# if normalized end < - Length??????????