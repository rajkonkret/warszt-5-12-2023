# # stworzyc system zarzadzanai biblioteka
# # dodaj ksiazke, usun ksiazke, wypozycz ksiazke, zwroc ksiazke
# # uzyc klass np.: Book, Library
# # obsłuzyc błedu
# # mozna dodac klase user - bedzie pamietał jakie ksiazki wypozyczył

# autor
# tytuł
# isbn
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author}, Tytuł: {self.title}, ISBN: {self.isbn}"


# liste ksiazek do wypozyczenia
# lista ksiazek wypozyczonych
# dodanie ksiazki do biblioteki
# wypozyczenie ksiazki
# zwróc ksiązke
# znajdz ksiazka
class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_ksiazki_wypozyczone(self):
        return self.wypozyczone_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        # usnac z dostepne
        # dodac do wypozyczone
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        return Exception("Nie mam takiej ksiązki")

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.append(book)
                self.wypozyczone_ksiazki.remove(book)
                return book
        return Exception("Ksiązka nie jest z naszej biblioteki")

    def fun_znajdz_ksiazke(self, isbn):
        # for book in self.dostepne_ksiazki:
        #     if book.isbn == isbn:
        #         return "Dostępne ksiązki", book
        # for book in self.wypozyczone_ksiazki:
        #     if book.isbn == isbn:
        #         return "Wypożyczone ksiązki", book

        dk, book_1 = self.przeszukaj_liste(self.dostepne_ksiazki, isbn)
        wk, book_2 = self.przeszukaj_liste(self.wypozyczone_ksiazki, isbn)
        if dk:
            return book_1, "Dostępne ksiązki"
        elif wk:
            return book_2, "Wypoyczone ksiązki"
        else:
            return Exception("Brak ksiązki")

    def przeszukaj_liste(self, lista, isbn):
        for book in lista:
            if book.isbn == isbn:
                return True, book
        return False, None


biblioteka = Library()
# biblioteka.fun_dodaj_ksiazke(Book("Programowanie w pythonie", "Jan Kowalski", "1234567890"))
# biblioteka.fun_dodaj_ksiazke(Book("Programowanie w pythonie dla zaawansowanch", "Jan Kowalski", "1234567891"))
# print("Dostępne ksiązki:", biblioteka.fun_ksiazki_do_wypozyczenia())
# print("Wypożyczone ksiązki:", biblioteka.fun_ksiazki_wypozyczone())
# print(biblioteka.fun_wypozycz_ksiazke('1234567890'))
# print("Dostępne ksiązki:", biblioteka.fun_ksiazki_do_wypozyczenia())
# print("Wypożyczone ksiązki:", biblioteka.fun_ksiazki_wypozyczone())
# # Dostępne ksiązki: [Author: Jan Kowalski, Tytuł: Programowanie w pythonie, ISBN: 1234567890,
# # Author: Jan Kowalski, Tytuł: Programowanie w pythonie dla zaawansowanch, ISBN: 1234567891]
# # Wypożyczone ksiązki: []
# # Author: Jan Kowalski, Tytuł: Programowanie w pythonie, ISBN: 1234567890
# # Dostępne ksiązki: [Author: Jan Kowalski, Tytuł: Programowanie w pythonie dla zaawansowanch, ISBN: 1234567891]
# # Wypożyczone ksiązki: [Author: Jan Kowalski, Tytuł: Programowanie w pythonie, ISBN: 1234567890]
# print(biblioteka.fun_znajdz_ksiazke("1234567890"))
# # ('Wypożyczone ksiązki', Author: Jan Kowalski, Tytuł: Programowanie w pythonie, ISBN: 1234567890)

while True:
    print(f"""
1. Dodaj ksiązke
2. Wypożycz ksiązkę
3. Pokaż dostępne
4. Znajdź ksiązkę
5. Koniec
""")
    odp = input("Podaj opcje")
    if odp == "1":
        autor = input("Podaj autora")
        tytul = input("Podaj tytuł")
        isbn = input("Podaj numer isbn")
        biblioteka.fun_dodaj_ksiazke(Book(tytul, autor, isbn))
        print("Ksiązka zostałą dodana")
    elif odp == "3":
        print(f"Dostępne ksiązki do wypożyczenia {biblioteka.fun_ksiazki_do_wypozyczenia()}")
    elif odp == "4":
        isbn = input("Podaj nuemr ISBN dla ksiązki")
        b, r = biblioteka.fun_znajdz_ksiazke(isbn)
        print(f"Ksiązka {b} jest w {r}")
    elif odp == "5":
        break
    else:
        print("Zła opcja")
