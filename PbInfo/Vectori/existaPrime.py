from random import randint


def prim(a):
    if a < 2:
        return 0
    elif a == 2:
        return 1
    elif a % 2 == 0:
        return 0
    else:
        i = 3
        while (i * i) <= a:
            if a % i == 0:
                return 0
            i += 2
        return 1


def main():
    n = int(input())
    array = input().split()
    for i in range(0, n):
        array[i] = int(array[i])

    for elem in array:
        if prim(elem):
            #print(elem)
            print("DA")
            exit(0)

    print("NU")


if __name__ == '__main__':
    main()

