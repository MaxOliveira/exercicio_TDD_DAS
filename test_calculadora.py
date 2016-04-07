import pytest
from calculadora import ClassCalsuladora

def test_calculadora():
    calc = ClassCalculadora
    assert calc.adicao(5,5) == 10
