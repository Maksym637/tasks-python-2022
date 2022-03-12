def fib_sum(n):
    if n <= 0:
        return 0
    else:
        fibon = [0] * (n + 1)
        fibon[0] = 0
        fibon[1] = 1
        sum = 1
        for i in range(2, n + 1):
            fibon[i] = fibon[i - 1] + fibon[i - 2]
            sum += fibon[i]
        return sum

n = 12
print(f"The sum of the first {n} Fibonacci numbers is {fib_sum(n)}")