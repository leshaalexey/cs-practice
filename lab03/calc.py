def plusplus(a, b):
    return a + b

def minusminus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def delen(a, b):
    if b != 0:
        return a / b
    else:
        return 0

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

if c == "/":
    d = delen(a, b)

print(d)
