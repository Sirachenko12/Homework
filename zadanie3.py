n = int(input("Podaj liczbę: "))
for i in range(n, n+1):
    for j in range(i):
        print(i, end="")
    print()
