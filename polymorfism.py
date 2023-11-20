from abc import ABC, abstractmethod

class Operation(ABC):
    def utför(self, num1, num2):
        pass

class Addition(Operation):
    def utför(self, num1, num2):
        return num1 + num2
    
class Subtraktion(Operation):
    def utför(self, num1, num2):
        return num1 - num2
    
class Multiplikation(Operation):
    def utför(self, num1, num2):
        return num1 * num2
    
class Kalkylator:
    def utför_operation(self, operation, num1, num2):
        return operation.utför(num1, num2)
    
    def main():
        addition = Addition()
        subtraktion = Subtraktion()
        multiplikation = Multiplikation()