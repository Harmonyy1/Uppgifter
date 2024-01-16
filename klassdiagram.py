class Djur():
    def __init__(self, namn):
        self.namn = namn

    def läte(self):
        pass

    def __str__(self):
        return f"{self.namn} låter såhär: {self.läte}"
    

        



class Däggdjur(Djur):
    def __init__(self, namn):
        super().__init__(namn)
        
    def läte(self):
        pass


class Kräldjur(Djur):
    def __init__(self, namn):
        super().__init__(namn)
    
    def läte(self):
        pass


class Fåglar(Djur):
    def __init__(self, namn):
        super().__init__(namn)

    def läte(self):
        pass



class Människa(Däggdjur):
    def __init__(self, namn):
        super().__init__(namn)

    def läte(self):
        return f"Hey you! What are you doing in my house!?"
    
    def to_string(self):
        return super().to_string()
    
    def print_info(self):
        super().print_info()
    


hooman = Människa("Akile")

hooman.print_info()



#Kolla mer på __str__ och fixa så att koden fungerar

