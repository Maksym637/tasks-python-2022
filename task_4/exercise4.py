def count_ones(n: int) -> int:
    binary = bin(n).replace("0b", "")
    count = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            count = count + 1
    return count

print(count_ones(255))