from func_tests.slice import my_slice


def test_slice_1():
    t_lst = [3,5,2,9]
    st = 1
    en = -1
    expected = [5,2]
    assert my_slice(t_lst, st, en) == expected


def test_slice_2():
    t_lst = [3,5,2,9]
    st = 1
    en = -100
    expected = []
    assert my_slice(t_lst, st, en) == expected


def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]