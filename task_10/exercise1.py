def rep(string: str) -> str:
    if string.find('"') != -1:
        return string.replace('"', "'")
    else:
        return string.replace("'", '"')

print(rep("A'B'C'D"))
print(rep(" ' ' ' "))

print(rep('A"B"C"D'))
print(rep(' " " " '))