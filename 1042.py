x = input().split()
n, n2, n3 = x
n = int(n)
n2 = int(n2)
n3 = int(n3)

array = [n, n2, n3]
sortedArray = sorted(array)

for i in sortedArray:
    print(i)

print("")

for i in array:
    print(i)
