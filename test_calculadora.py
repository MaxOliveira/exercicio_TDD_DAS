import pytest
from calculadora import ClassCalculadora

def test_calculadora():
    calc = ClassCalculadora()
    assert calc.adicao(5,5) == 10
