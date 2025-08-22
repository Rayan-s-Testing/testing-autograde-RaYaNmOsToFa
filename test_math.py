import mathematics

#this is going to test the mathematics.py file

def test_addition():
    m = mathematics.Mathematics()
    assert m.add(2, 3) == 5
    assert m.add(-1, 1) == 0
    assert m.add(0, 0) == 0

def test_subtract():
    m = mathematics.Mathematics()
    assert m.subtract(2, 3) == -1
    assert m.subtract(-1, 1) == -2
    assert m.subtract(0, 0) == 0

def test_multiply():
    m = mathematics.Mathematics()
    assert m.multiply(2, 3) == 6
    assert m.multiply(-1, 1) == -1
    assert m.multiply(0, 0) == 0

def test_divide():
    m = mathematics.Mathematics()
    t = 2/3
    assert m.divide(2, 3) == t
    assert m.divide(-1, 1) == -1
    try:
        assert m.divide(0, 0) == 0
    except:
        assert True
