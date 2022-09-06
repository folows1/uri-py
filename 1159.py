n = -1

while (n != 0):
    n = int(input())
    if (n == 0):
        break
    if (n % 2 == 0):
        print("{}".format(n * 5 + 20))
    else:
        print("{}".format((n + 1) * 5 + 20))
