list_of_digits = [4, -9, 8, -11, 8]
negative_count = len(list(filter(lambda x: (x < 0), list_of_digits)))
print(negative_count)