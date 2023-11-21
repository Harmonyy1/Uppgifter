from abc import ABC, abstractmethod     #importerar för att kunna skapa abstrakta klasser


class Operation(ABC):   #basklass
    @abstractmethod        #abstrakt metod
    def utför(self, num1, num2):
        pass



class Addition(Operation):  #subklass

    def utför(self, num1, num2):
        return num1 + num2      #returnerar värdet av argumenten efter addition
    
class Subtraktion(Operation):

    def utför(self, num1, num2):
        return num1 - num2      #subtraktion
    
class Multiplikation(Operation):    

    def utför(self, num1, num2):
        return num1 * num2      #multiplikation
    
class Kalkylator:   #ny klass som använder operationklasserna
    def utför_operation(self, operation, num1, num2):
        return operation.utför(num1, num2)
    
    
def main():     #sätter operationklasserna under variabler
    addition = Addition()
    subtraktion = Subtraktion()
    multiplikation = Multiplikation()
    kalkylator = Kalkylator()

    print("Addition: ", kalkylator.utför_operation(addition, 10, 5))    #anvädner metoden utför_operation där operation ersätts med en av operationsklasserna
    print("Subtraktion: ", kalkylator.utför_operation(subtraktion, 10, 5))
    print("Multiplikation: ", kalkylator.utför_operation(multiplikation, 10, 5))

#kör huvudfunktionen
if __name__ == "__main__":
    main()