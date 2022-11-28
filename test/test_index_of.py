from func_tests.index_of import index_of

def test_index_of_1():
    t_lst = [1,2,3,4]
    val = 4
    idex = 2
    expected = 3
    assert index_of(t_lst,val,idex) == expected


def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([1,2,3,4], 0, 5) == -1