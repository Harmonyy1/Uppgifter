#Uppgift 1

class Bankkonto():
    def __init__(self, namn, saldo = 0):
        self.__namn = namn
        self.__saldo = saldo

    def sätta_in(self, belopp):
        self.__saldo += belopp
        print(f"{belopp} kr har satts in på ditt konto.")

    def ta_ut(self, belopp):
        if self.__saldo >= belopp:
            self.__saldo -= belopp
            print(f"{belopp} kr har tagits från ditt konto")
        else:
            print(f"Inga bengar :(")

    def visa_saldo(self):
        print(f"Saldo: {self.__saldo}")


konto = Bankkonto("Gojo Satoru", 7350)
konto.sätta_in(1000)
konto.ta_ut(1500)
konto.visa_saldo()


#Uppgift 2

class Studerande():
    def __init__(self, namn, ålder, betyg):
        self.__namn = namn
        self.__ålder = ålder
        self.__betyg = betyg

    