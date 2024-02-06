class Djur():
    def __init__(self, namn):
        self.namn = namn
        self.läte = "Djur kan ha många olika läten!"

    def to_string(self):
        return f"{self.namn} låter såhär: {self.läte}"
    
    def print_info(self):
        print(self.to_string())

        



class Däggdjur(Djur):
    def __init__(self, namn):
        super().__init__(namn)


class Kräldjur(Djur):
    def __init__(self, namn):
        super().__init__(namn)


class Fåglar(Djur):
    def __init__(self, namn):
        super().__init__(namn)

        
        

class Människa(Däggdjur):
    def __init__(self, namn):
        super().__init__(namn)
        self.läte = "Hey you! What are you doing in my house!?"
        

    def to_string(self):
        return super().to_string()
    
    def print_info(self):
        super().print_info()
    


hooman = Människa("Akile")

hooman.print_info()