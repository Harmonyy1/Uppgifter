#Uppgift 1
"""
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
"""

#Uppgift 2

class Studerande:
    def __init__(self, namn, ålder, betyg):
        self.__namn = namn
        self.__ålder = ålder if ålder > 0 else 18
        self.__betyg = []

    def lägga_till_betyg(self, betyg):
        if 0 <= betyg <= 100:
            self.__betyg.append(betyg)
        else: 
            print("ERROR - betyget måste vara mellan 1 - 100!")

    def medelbetyg(self, betyg):
        return sum(self.__betyg) / len(self.__betyg) if self.__betyg else 0
    
    def sätt_info(self, namn, ålder):
        self.__namn = namn
        self.__ålder = ålder if ålder > 0 else self.__ålder

    def få_info(self):
        return self.__namn, self.__ålder, self.medelbetyg()
    
class Studerandehantering:
    def __init__(self):
        self.__studerandelista = []

    def lägga_till_studerande(self, studerande):
        self.__studerandelista.append(studerande)

    def ta_bort_studerande(self, namn):
	        self.__studerandelista = [s for s in self.__studerandelista if s.få_info()[0] != namn]



hanterare = Studerandehantering()
studerande1 = Studerande("Alice", 20, 78)
studerande1.lägga_till_betyg(85)
studerande1.lägga_till_betyg(90)
hanterare.lägga_till_studerande(studerande1)
studerande2 = Studerande("Bob", 22, 65)
studerande2.lägga_till_betyg(92)
studerande2.lägga_till_betyg(88)	
hanterare.lägga_till_studerande(studerande2)