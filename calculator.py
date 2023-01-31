import operator


def dej_number(a):
    return float(a)



def dodawanie(y, x):
    return operator.add(dej_number(y), dej_number(x))


def odejmowanie(y, x):
    return operator.sub(dej_number(y), dej_number(x))


def dzielenie(y, x):
    return operator.truediv(dej_number(y), dej_number(x))


def mnozenie(y, x):
    return operator.mul(dej_number(y), dej_number(x))


def main():
    w = 0
    x = input("podaj pierwsza liczbe: ")
    z = input("podaj znak dzialania: ")
    y = input("podaj druga liczbe: ")

    if z == "+":
        w = dodawanie(x, y)
    elif z == "-":
        w = odejmowanie(x, y)
    elif z == "*":
        w = mnozenie(x, y)
    elif z == "/":
        w = dzielenie(x, y)

    print(w)


if __name__ == '__main__':
    main()
