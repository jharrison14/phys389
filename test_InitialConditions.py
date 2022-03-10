import pytest
import InitialConditions as ic

def test_line():
    assert ic.line(2,3,4) == 10


