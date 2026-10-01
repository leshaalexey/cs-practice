def plusplus(a, b):
    return a + b

a = float(input())
b = float(input())
c = input("выберите из ( * - + )")

d = 0
if c == "+":
    d = plusplus(a, b)
