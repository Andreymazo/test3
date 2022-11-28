from func_tests.get import get

def test_get_1():
    t_lst = [1,2,3]
    key = 2
    expected = 3
    assert get(t_lst,key) == expected

def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"
    assert get([1, 2, 3], -5) == None
    assert get([1, 2, 3], 0) == 1


