print("Nazywam się Radek")
print(type("Radek"))  # <class 'str'>
print('Nazywam się Radek')
# pep8 - zasady pisania czystego kodu w pythonie
print(39)
print(type(39))  # <class 'int'> całkowite
print("93")
print(type("93"))  # <class 'str'>
print("93" + "39")  # konkatenacja (łaczenie tekstów)
# ctr alt l
print(5 * "Radek")  # RadekRadekRadekRadekRadek
print(14 + 78)  # 92
# zmienna
# pudełko na dane
# musi miec nazwe
# typowanie dynamiczne
name = "Radek"
print(type(name))  # <class 'str'>
# snake_case
print(name)  # Radek
name = 39
print(name)
print(type(name))  # <class 'int'>
# print("14" + 45)  # TypeError: can only concatenate str (not "int") to str
# ctrl / - szybki komentarz
print(int("14") + 45)  # 59

wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowe
temp2 = 36, 6  # to nie jest liczba

print(0.1 + 0.5)
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# przy float wystepuje bład zaokrąglenie
# decimal - to obliczeń bez błedu zaokrąglenia

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # float
print(wiek // rok)  # dziellenie bez reszty
print(wiek ** rok)
print(len(str(wiek ** rok)))  # 3383 tyle znakw ma wynik tego działania

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)

wersja = 3.9000001
print(f"Używamy wersji pythona {wersja}")  # f-string Używamy wersji pythona 3.9000001
print("Używamy {}".format(wersja))
print("Używamy %f" % wersja)  # Używamy 3.900000
print("Używamy %.2f" % wersja)  # Używamy 3.90
# zaokraglają przy wyswietlaniu
# wersja z % - weryfikuje typ
# print("Uzywamy %f" % "wersja")  # TypeError: must be real number, not str
print("tekst:", wersja)  # tekst: 3.9000001
"""
   Prints the values to a stream, or to sys.stdout by default.

     sep
       string inserted between values, default a space.
     end
       string appended after the last value, default a newline.
     file
       a file-like object (stream); defaults to the current sys.stdout.
     flush
       whether to forcibly flush the stream.
   """
print("tekst:", wersja, sep="()")  # tekst:()3.9000001

print("""
Tekst 
    wielolinijkowy
""")
# "Tekst
#     wielolinijkowy"

imie = "Radek Radek"
imie.upper()  # upper() - zamiana na duże litery
# teksty w pythonie są immutable
print(imie)  # Radek Radek
tekst2 = imie.upper()
print(tekst2)  # RADEK RADEK
print(imie)  # Radek Radek

liczba = 456123789345
print(liczba)
print(f"Nasza duża {liczba:,}")  # Nasza duża 456,123,789,345
print(f"Nasza duża {liczba:,}".replace(",", "."))  # Nasza duża 456.123.789.345

# typ logiczny
# 11:30
