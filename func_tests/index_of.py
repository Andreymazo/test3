# Функция `index_of(list, value, from_index)` возвращает первый индекс, по которому переданное значение может
# быть найдено в списке или `-1`, если такого значения нет.

# Аргументы:
#
# - `list` - список, в котором ведется поиск.
# - `value` - значение, поиск которого ведется в массиве .
# - `from_index` - индекс, с которого начинается поиск элемента, по умолчанию равен нулю. Если значение `from_index` отрицательное, то оно используется, как смещение с конца массива.

def index_of(coll, value, from_index=0):
    length = len(coll)

    if length == 0:
        return -1

    index = from_index

    if index < 0:
        if index < -length:
            index = 0
        else:
            index += length

    try:
        return coll.index(value, index)
    except ValueError:
        return -1

numbers = [1, 2, 3, 2, 5]
index_of(numbers, 2)  # 1
index_of(numbers, 7)  # -1
index_of(numbers, 2, -3)  # 3