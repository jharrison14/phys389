import pytest

def line(x,m,c):
    return m*x + c

def test_line():
    assert line(2,3,4) == 10


