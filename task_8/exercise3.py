def MultArithmeticElements(a1: int, t: int, n: int) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return a1
    else:
        an = 0
        mult = 1
        for i in range(0, n):
            an = a1
            a1 += t
            mult *= an
        return mult