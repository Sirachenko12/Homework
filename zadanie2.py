figure = input("Wybierz figure (1-Prostokąt, 2-Trójkąt, 3-Koło, 4-Kwadrat): ")

if figure == '1':
    a = float(input("a = "))
    b = float(input("b = "))
    print("Obwód", ((a + b) * 2))
    print("Pole", (a * b))



elif figure == '2':
    print("Podaj liczby")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    h = float(input("h = "))
    print("Obwod", (a + b + c))
    print("Pole", ((a * h) / 2))

elif figure == '3':
    r = float(input("r = "))

    print("Obwod", ((2 * 3.14) * r))
    print("Pole", (3.14 * (r ** 2)))

elif figure == "4":
    a = float(input("a = "))

    print("Obwod", (a * 4))
    print("Pole", (a * a))


else:
    print()

