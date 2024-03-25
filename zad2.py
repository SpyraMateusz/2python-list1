class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_author(self):
        return self.author

    def set_author(self, new_author):
        self.author = new_author

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year
        
        
        
        
        
        
        
        
        # a to przykład importowania klasy Book z modułu book
        from    book import Book

# Tworzenie instancji książki
my_book = Book("Tytuł Książki", "Autor Książki", 2022)

# Pobieranie i wyświetlanie atrybutów książki
print("Tytuł:", my_book.get_title())
print("Autor:", my_book.get_author())
print("Rok wydania:", my_book.get_year())

# Zmiana tytułu książki i wyświetlenie nowego tytułu
my_book.set_title("Nowy Tytuł Książki")
print("Nowy tytuł:", my_book.get_title())