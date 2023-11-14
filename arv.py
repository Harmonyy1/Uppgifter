class Video():  #skapar basklassen Video
    
    def __init__(self, title, length):  #konstruktor

        self.title = title  #instansattribut
        self.length = length

    def to_string(self):    #konstruktor som används sätter in information i en string
        return f"{self.title} is {self.length} minutes long"    #returnerar en string
    
    def print_info(self):   #konstruktor som används senare för att printa
        print(self.to_string())

    
class Movie(Video):     #subklass av klassen Video

    def __init__(self, title, length, director, rating):
        super().__init__(title, length)     #tar information från basklassen

        self.director = director    #unika instansattribut för subklassen
        self.rating = rating

    def to_string(self):
        return super().to_string() + f" and has the director {self.director} and the rating {self.rating}"
    
    def print_info(self):
        super().print_info()

class WebVideo (Video):     #subklass för basklassen Video
    def __init__(self, title, length, likes, dislikes, comments):
        super().__init__(title, length)
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments

    def to_string(self):
        return super().to_string() + f" has {self.likes} likes, {self.dislikes} dislikes and {self.comments} comments"
    
    def print_info(self):
        super().print_info()

    
        


vid1 = Video("liv jobbar inte: the video", "165")   #sätter klasser under en variabel med de värden som ska sättas in i instansattributen

mov1 = Movie("liv jobbar inte: the movie", "165", "gabbe", "10/10")

webvid1 = WebVideo("liv jobbar inte (vlog)", "165", "69", "0", "321")

vid1.print_info()   #använder konstruktorn print_info för att skriva ut det som finns under "to_string" så som det är angett i "print_info"
mov1.print_info()
webvid1.print_info()