def plusplus(a, b):
    return a + b

def minusminus(a, b):
    return a - b

def multiply(a, b):
    return a * b

a = float(input())
b = float(input())
c = input("выберите из ( * - + )")

d = 0
if c == "+":
    d = plusplus(a, b)

if c == "-":
    d = minusminus(a, b)

if c == "*":
    d = multiply(a, b)

print(d)
