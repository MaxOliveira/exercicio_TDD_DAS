import pytest
from calculadora import ClassCalculadora

def test_calculadora():
    calc = ClassCalculadora()
    assert calc.adicao(5,5) == 10

def test_calculadora_subtracao():
    calc = ClassCalculadora()
    assert calc.subtracao(10, 4) == 6

def test_calculadora_multiplicacao():
    calc = ClassCalculadora()
    assert calc.multiplicacao(10, 2) == 20

def test_calculadora_divisao():
    calc = ClassCalculadora()
    assert calc.divisao(10, 2) == 5
