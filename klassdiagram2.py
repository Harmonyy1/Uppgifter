#Uppgift 2

class Library():
    def __init__(self):
        pass

    def add_book(self, title, author):
        self.title = title
        self.author = author

    def remove_book(self, book):
        self.book = book

    def register_member(self, name):
        self.name = name

    def find_book_by_title(self, title):
        self.title = title
        return self.book or None            #troligen fel här
    


class Bok(Library):
    def __init__(self):
        pass

    def check_out(self):
        