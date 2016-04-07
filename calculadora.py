import math

class ClassCalculadora():

    def adicao(self, x, y):
      return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def potencia(self, x, y):
        return x ** y

    def radical(self, x, y):
        radical = x ** (1 / y)
        return radical

    def log(self, x, y):
        log = math.log(x, y)
        return log

    def fatorial(self, x):
        if x <= 1:
            return 1
        else:
            return x * self.fatorial(x - 1)
