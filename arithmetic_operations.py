from abc import ABC, abstractmethod


class ArithmeticOperation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(ArithmeticOperation):
    def execute(self, a, b):
        return a + b


class Subtraction(ArithmeticOperation):
    def execute(self, a, b):
        return a - b


class Multiplication(ArithmeticOperation):
    def execute(self, a, b):
        return a * b


class Division(ArithmeticOperation):
    def execute(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
