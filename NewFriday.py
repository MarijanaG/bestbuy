def square(num: int)-> int:
    result = num * num
    return result


def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-2) == 3



