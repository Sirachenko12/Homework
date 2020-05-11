
for i in range(0, 100, 1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print("Hot Fizz Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 2 == 0 and i % 3 == 0:
        print("Hot Fizz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 2 == 0 and i % 5 == 0:
        print("Hot Buzz")
    elif i % 2 == 0:
        print("Hot")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)