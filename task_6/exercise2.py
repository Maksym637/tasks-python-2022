def information(**kwargs):
    print("\nData type of argument : ", type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


information(Name="Max", Age=19, Phone=123456789)

d = {"Name": "Tom", "Age": 12, "Phone": 223456789, "Pet": "Cat"}  
information(**d)