def SumGeometricElements(a1: float, t: float, alim: float) -> float:
    if t > 0 and t < 1:
        sum = 0
        while a1 > alim:
            an = a1
            a1 *= t
            sum += an
        return sum
    else:
        return 0