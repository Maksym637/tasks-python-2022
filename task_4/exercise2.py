def factorial_1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_1(n - 1)

def factorial_2(n):
    res = 1
    if n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
    return res


try:
    n = int(input("n = "))
    print("n! = " + str(factorial_2(n)))
except:
    print("Incorrect value!")