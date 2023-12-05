try:
    # print("12" + 34)
    # print(34 / 0)
    print(int("A"))
    # print("A")
except TypeError:
    print("Bład typu")
except ZeroDivisionError:
    print("Nie dziel przez zero")
except Exception as e:
    print("Bład", e)
else:
    print("Wykona się gdy nie ma błedu")
finally:
    print("Wykona się zawsze")

print("Dalsza częśc programu")
