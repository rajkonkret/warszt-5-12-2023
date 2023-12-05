# funkcja wewnętrzna
# zasadę dziłania funkcji wewnętrnej w pythonie wykorzystuja dekorator
# @dekorator

def fun1(c):
    print(f"To jest fun1 {c}")

    def fwew(a, b):
        return a * b

    return fwew  # zwracamy adres funkcji (referencje)


xFun = fun1("radek")
print(xFun)  # <function fun1.<locals>.fwew at 0x000001F20B90CF40>
print(xFun(3, 5))  # 15
# To jest fun1 radek
# <function fun1.<locals>.fwew at 0x00000192ADC3CF40>
# 15
