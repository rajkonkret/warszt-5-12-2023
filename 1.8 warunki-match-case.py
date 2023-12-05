# match case - instrukcja warunkowa

lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "java":
        print("Java")
    case "python":
        print("Python")
    case _:  # domyslna wartosć (else)
        print("Domyslna")
