x = input().split()
a, b = x
a = int(a)
b = int(b)

if a == 0 and b == 0:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if b > a:
        r = b - a
        print("O JOGO DUROU {} HORA(S)".format(r))
    else:
        r = 24 - (a - b)
        print("O JOGO DUROU {} HORA(S)".format(r))
