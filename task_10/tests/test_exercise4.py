from exercise4 import test_1_1 as t_1, test_1_2 as t_2, test_1_3 as t_3, test_1_4 as t_4

s1 = ["hello", "world", "python"]
s2 = ["dog", "cat", "kitten", "puppy"]
s3 = ["acd", "akl"]
s4 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s5 = []

def test_1():
    assert t_1(*s1) == {'o'}
    assert t_1(*s2) == set()
    assert t_1(*s3) == {'a'}
    assert t_1(*s4) == set()
    assert t_1(*s5) == 0

def test_2():
    assert t_2(*s1) == {'d', 'e', 'n', 'p', 'r', 't', 'w', 'y'}
    assert t_2(*s2) == {'c', 'n', 'o', 'i', 'g', 'd', 'u', 'p', 'a', 'k', 'y', 'e'}
    assert t_2(*s3) == {'l', 'c', 'd', 'k'}
    assert t_2(*s4) == set(s4)
    assert t_2(*s5) == 0

def test_3():
    assert t_3(*s1) == {'h', 'l', 'o'}
    assert t_3(*s2) == {'t'}
    assert t_3(*s3) == {'a'}
    assert t_3(*s4) == set()
    assert t_3(*s5) == 0

def test_4():
    assert t_4(*s1) == {'a','b','c','f','g','i','j','k','m','q','s','u','v','x','z'}
    assert t_4(*s2) == {'b','f','h','j','l','m','q','r','s','v','w','x','z'}
    assert t_4(*s3) == {'b','e','f','g','h','i','j','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    assert t_4(*s4) == set()
    assert t_4(*s5) == 0