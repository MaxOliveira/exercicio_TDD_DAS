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

def test_calculadora_potencia():
    calc = ClassCalculadora()
    assert calc.potencia(2, 2) == 4

def test_calculadora_radical():
    calc = ClassCalculadora()
    assert calc.radical(9, 2.0) == 3

def test_calculadora_log():
    calc = ClassCalculadora()
    assert calc.log(4, 2) == 2

def test_calculadora_fatorial():
    calc = ClassCalculadora()
    assert calc.fatorial(5) == 120

def test_calculadora_valor_absoluto():
    calc = ClassCalculadora()
    assert calc.valorAbsoluto(10) == 10
