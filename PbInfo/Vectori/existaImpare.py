n = int(raw_input())
array = raw_input().split()

for i in range(0, n):
    array[i] = int(array[i])

for elem in array:
    if elem % 2 == 1:
        print("DA")
	exit()

print("NU")
