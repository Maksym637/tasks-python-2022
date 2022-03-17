from exercise1 import Rectangle, ArrayRectangles

rectangle1 = Rectangle(40, 30)
rectangle2 = Rectangle(11, 20)
rectangle3 = Rectangle(200, 200)
rectangle4 = Rectangle(4, 4)
rectangle5 = Rectangle(17, 18)        

def test_ArrayRectangles_1():
    rectangles_1 = ArrayRectangles(0)
    rectangles_2 = ArrayRectangles(-4)
    assert rectangles_1.AddRectangle(rectangle1) == False
    assert rectangles_2.AddRectangle(rectangle2) == False

def test_ArrayRectangles_2():
    rectangles = ArrayRectangles(3)
    assert rectangles.AddRectangle(rectangle1) == True
    assert rectangles.AddRectangle(rectangle2) == True
    assert rectangles.AddRectangle(rectangle3) == True
    assert rectangles.AddRectangle(rectangle4) == False

    assert rectangles.NumberMaxArea() == 2
    assert rectangles.NumberMinPerimeter() == 1
    assert rectangles.NumberSquare() == [2]

def test_ArrayRectangles_3():
    rectangles = ArrayRectangles(5)
    assert rectangles.AddRectangle(rectangle1) == True
    assert rectangles.AddRectangle(rectangle2) == True
    assert rectangles.AddRectangle(rectangle3) == True
    assert rectangles.AddRectangle(rectangle4) == True
    assert rectangles.AddRectangle(rectangle5) == True
    assert rectangles.AddRectangle(rectangle1) == False
    assert rectangles.AddRectangle(rectangle1) == False

    assert rectangles.NumberMaxArea() == 2
    assert rectangles.NumberMinPerimeter() == 3
    assert rectangles.NumberSquare() == [2, 3]

def test_ArrayRectangles_4():
    rectangles = ArrayRectangles(7)
    assert rectangles.AddRectangle(rectangle1) == True
    assert rectangles.AddRectangle(rectangle2) == True
    assert rectangles.AddRectangle(rectangle3) == True
    assert rectangles.AddRectangle(rectangle4) == True
    assert rectangles.AddRectangle(rectangle5) == True
    assert rectangles.AddRectangle(rectangle3) == True
    assert rectangles.AddRectangle(rectangle4) == True

    assert rectangles.NumberMaxArea() == 2
    assert rectangles.NumberMinPerimeter() == 3
    assert rectangles.NumberSquare() == [2, 3, 5, 6]