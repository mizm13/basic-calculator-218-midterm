""" File: test_main.py """
import pytest
from app.main import add, subtract, multiply, divide

def test_add():
    """Addition function"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Subtraction function"""
    assert subtract(1, 1) == 0

def test_multiply():
    """Multiply function"""
    assert multiply(1, 3) == 3

def test_divide():
    """Divide function"""
    assert divide(4, 2) == 2

def test_divide_by_zero():
    """Test division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
