from calculator import add
from calculator import subtract


def test_add():
    assert add(2,3) == 5
    
def test_subtract():
    assert subtract(5, 2) == 3
    