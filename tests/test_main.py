# File: test_main.py
import sys
import os

# Add the parent directory (project root) to sys.path so 'main.py' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the 'add' function
from main import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
