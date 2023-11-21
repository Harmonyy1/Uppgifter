#Uppgift 1

class Bankkonto():      #basklass
    def __init__(self, namn, saldo = 0):    #privata attribut
        self.__namn = namn
        self.__saldo = saldo

    def sätta_in(self, belopp):     #metod för att öka värdet på belopp
        self.__saldo += belopp
        print(f"{belopp} kr har satts in på ditt konto.")

    def ta_ut(self, belopp):    #metod för att ta ut pengar
        if self.__saldo >= belopp:  #if-sats
            self.__saldo -= belopp
            print(f"{belopp} kr har tagits från ditt konto")
        else:
            print(f"Inga bengar :(")

    def visa_saldo(self):       #printar saldo
        print(f"Saldo: {self.__saldo}")

#testar klassen
konto = Bankkonto("Gojo Satoru", 7350)
konto.sätta_in(1000)
konto.ta_ut(1500)
konto.visa_saldo()


#Uppgift 2

class Studerande:
    def __init__(self, namn, ålder, betyg):     #privata attribut
        self.__namn = namn
        self.__ålder = ålder if ålder > 0 else 18
        self.__betyg = []   #privat lista

    def lägga_till_betyg(self, betyg):  #metod för att lägga till betyg
        if 0 <= betyg <= 100:   #if-sats
            self.__betyg.append(betyg)  #lägger in i lista
        else: 
            print("ERROR - betyget måste vara mellan 1 - 100!")

    def medelbetyg(self, betyg):    #metod för medelvärde av betyg
        return sum(self.__betyg) / len(self.__betyg) if self.__betyg else 0
    
    def sätt_info(self, namn, ålder):
        self.__namn = namn
        self.__ålder = ålder if ålder > 0 else self.__ålder

    def få_info(self):
        return self.__namn, self.__ålder, self.medelbetyg()
    
class Studerandehantering:  #klass
    def __init__(self):
        self.__studerandelista = []     #privat lista

    def lägga_till_studerande(self, studerande):    #metod som sätter in i lista
        self.__studerandelista.append(studerande)

    def ta_bort_studerande(self, namn):     #metod som tar bort från lista
	        self.__studerandelista = [s for s in self.__studerandelista if s.få_info()[0] != namn]


#testar klasser
hanterare = Studerandehantering()
studerande1 = Studerande("Alice", 20, 78)
studerande1.lägga_till_betyg(85)
studerande1.lägga_till_betyg(90)
hanterare.lägga_till_studerande(studerande1)
studerande2 = Studerande("Bob", 22, 65)
studerande2.lägga_till_betyg(92)
studerande2.lägga_till_betyg(88)	
hanterare.lägga_till_studerande(studerande2)