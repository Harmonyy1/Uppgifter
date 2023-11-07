class Video():  #skapar basklassen Video
    
    def __init__(self, title, length):

        self.title = title
        self.length = length

    def to_string(self):
        return f"{self.title} is {self.length} minutes long"
    
    def print_info(self):
        print(self.to_string())

    
class Movie(Video):
    def __init__(self, title, length, director, rating):
        super().__init__(title, length)

        self.director = director
        self.rating = rating

    def to_string(self):
        return super().to_string() + f" and has the director {self.director} and the rating {self.rating}"
    
    def print_info(self):
        super().print_info()

class WebVideo (Video):
    def __init__(self, title, length, likes, dislikes, comments):
        super().__init__(title, length)
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments

    def to_string(self):
        return super().to_string() + f" has {self.likes} likes, {self.dislikes} dislikes and {self.comments} comments"
    
    def print_info(self):
        super().print_info()

    
        


vid1 = Video("liv jobbar inte: the video", "165")

mov1 = Movie("liv jobbar inte: the movie", "165", "gabbe", "10/10")

webvid1 = WebVideo("liv jobbar inte (vlog)", "165", "69", "0", "321")

vid1.print_info()
mov1.print_info()
webvid1.print_info()