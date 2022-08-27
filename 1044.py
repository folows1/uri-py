x = input().split()
a, b = x
a = int(a)
b = int(b)
if a > b:
    r = a % b
else:
    r = b % a
if (r == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
