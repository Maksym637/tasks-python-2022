from exercise2 import multiplicity

def test_multiplicity_3():
    assert multiplicity(3) == "Fizz"
    assert multiplicity(18) == "Fizz"
    assert multiplicity(99) == "Fizz"

def test_multiplicity_5():
    assert multiplicity(5) == "Buzz"
    assert multiplicity(55) == "Buzz"
    assert multiplicity(70) == "Buzz"

def test_multiplicity_3_and_5():
    assert multiplicity(15) == "FizzBuzz"
    assert multiplicity(30) == "FizzBuzz"
    assert multiplicity(75) == "FizzBuzz"

def test_multiplicity_number():
    assert multiplicity(4) == 4
    assert multiplicity(19) == 19
    assert multiplicity(37) == 37
    assert multiplicity(91) == 91