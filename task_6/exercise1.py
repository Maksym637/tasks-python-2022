def average(*args: int) -> float:
    sum = 0
    cnt = 0
    result = 0

    for i in args:
        sum += i
        cnt = cnt + 1
    
    result = sum / cnt

    return "{:.2f}".format(result)

print(average(2, 3, 4, 100, 12, 7, 8, 0))