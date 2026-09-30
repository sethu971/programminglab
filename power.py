n = int(input("Enter any positive number: "))
e = int(input("Enter the value of exponent: "))
p = 1

for i in range(1, e + 1):
    p = p * n

print("The power of", n, "^", e, "is", p)