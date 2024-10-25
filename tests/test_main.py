""" File: test_main.py """
from app.main import add, subtract, multiply, divide

def test_add():
    """Addition function"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_subtract():
    """Addition function"""
    assert subtract(1, 1) == 0
    
    
def test_multiply():
    """Multiply function"""
    assert multiply(1, 3) == 3
    

def test_divide():
    """Divide function"""
    assert divide(4, 2) == 2

