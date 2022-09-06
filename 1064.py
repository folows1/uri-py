n = 0
avr = 0

for i in range(6):
    a = float(input())
    if a > 0:
        n += 1
        avr += a

print("{} valores positivos".format(n))
print("{:.1f}".format(avr/n))
