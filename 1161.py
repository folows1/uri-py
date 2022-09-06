while True:
    try:

        a, b = map(int, input().split())

        s1 = 1
        s2 = 1

        if (a != 0):
            for i in range(1, a+1):
                s1 *= i

        if (b != 0):
            for i in range(1, b+1):
                s2 *= i

        print("{}".format(s1 + s2))

    except:
        break
