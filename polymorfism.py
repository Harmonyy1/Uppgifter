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
    kalkylator = Kalkylator()

    print("Addition: ", kalkylator.utför_operation(addition, 10, 5))    #är "operation" bara en placeholder för där något av räknesätten ska sättas in?
    print("Subtraktion: ", kalkylator.utför_operation(subtraktion, 10, 5))
    print("Multiplikation: ", kalkylator.utför_operation(multiplikation, 10, 5))

if __name__ == "__main__":
    main()