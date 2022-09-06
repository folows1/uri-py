array = []
for i in range(10):
    array.append(int(input()))

for i in range(10):
    if (array[i] <= 0):
        print("X[{}] = 1".format(i))
    else:
        print("X[{}] = {}".format(i, array[i]))
