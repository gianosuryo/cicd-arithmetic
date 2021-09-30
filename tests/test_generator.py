import random

from arithmetic import generator

def test_division_basic():
    x = random.randint(-100, 100);
    y = random.randint(-100, 100);
    res_division = generator.division(x, y)

    assert type(res_division) == int or float

def test_division_type():
    res_division_1 = generator.division('a', 2)
    res_division_2 = generator.division(32, 'd')

    assert type(res_division_1) == int or float
    assert type(res_division_2) == int or float

def test_division_by_zero():
    res_division = generator.division(2, 0)
    assert type(res_division) == int or float