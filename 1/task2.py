import math

try:
    N = int(input("Enter number amount: "))
except ValueError:
    exit("Value Error!")

for x in range(N + 1):
    for y in range(N + 1):
        if x+y == 0:
            print(" ", end=" ")
        elif x == 0 or y == 0:
            print(x+y, end=" ")
        else:
            if math.gcd(x, y) == 1:
                print("X", end=" ")
            else:
                print("0", end=" ")
    print("\n")