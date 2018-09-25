from .. import Array

arr = Array([5,8,-4])
arr2 = Array([-8, 10, 15])

def test_sum():
    assert arr.sum() == 9
    assert arr2.sum() == 17

def test_min():
    assert arr.min() == -4
    assert arr2.min() == -8

def test_max():
    assert arr.max() == 8
    assert arr2.max() == 15
