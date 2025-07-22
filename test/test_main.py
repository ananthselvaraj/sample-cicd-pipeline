from src.main import add,sub


def test_add():
    assert add(10,10) == 20
    assert add(1,1) == 2

def test_sub():
    assert sub(10,10) == 0
    assert sub(4,2) == 2
    assert sub(7,8) == -1
    assert sub(5,3) == 2
    assert sub(11,10) == 1