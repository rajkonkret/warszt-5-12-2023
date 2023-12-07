def powitanie():
    print("Powitanie")


def info():
    print("Jestem pakietem")


# jesli bezposrednio uruchomimy plik to ta komenda sie wykona
# nie bedzie wykonan ta komenda podczas importu
if __name__ == '__main__':
    powitanie()
