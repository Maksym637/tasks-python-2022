import math as m

def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = m.sqrt(p * (p - a) * (p - b) * (p - c))
        s_precision_2 = "{:.2f}".format(s)
        return s_precision_2
    else:
        return -1

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(f's = {triangle_area(a, b, c)}')
except:
    print("This is not a value!")