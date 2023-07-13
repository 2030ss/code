def isnarci(i):
    if i < 100 or i >= 1000:
        print(i, "不是水仙花数")

    else:
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        if a**3 + b**3 + c**3 == i:
            print(i, "是水仙花数")
        else:
            print(i, "不是水仙花数")


def isprime(j):
    if j == 1:
        print(j, "不是素数")
        return False
    elif j == 2:
        print(j, "是素数")
        return True
    else:
        for x in range(2, j):
            if (j % x) == 0:
                print(j, "不是素数")
                return False
        print(j, "是素数")
        return True
