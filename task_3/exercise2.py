def multiplicity(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print("Input number from 1 to 100")
try:
    number = int(input("number = "))
    print(multiplicity(number))
except:
    print("Not valid value")
