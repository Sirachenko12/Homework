print("Podaj liczbę od 1 do 100: ")
n = int(input())
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print("Podana liczba nie jest liczbą pierwsza")
            break
    else:
        print("Podana liczba jest liczbą pierwszą")

else:
    print(n, "Podabna liczba nie jest liczbą pierwszą")