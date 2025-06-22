from main import main


# Только положительные числа
def test_only_pos_1():
    res = main([10, 3, 2])
    assert res == 5


def test_only_pos_2():
    res = main([1, 3, 4])
    assert res == 2.67


# Только отрицательные числа
def test_only_neg_1():
    res = main([-1, -2, -3])
    assert res == -2


def test_only_neg_2():
    res = main([-7, -2, -1, -2])
    assert res == -3


# Пустой список
def test_none():
    res = main([])
    assert res is None
