class Rectangle():
    def __init__(self, a: int, b: int = 5) -> None:
        self.__a = a
        self.__b = b
    
    def __str__(self) -> str:
        return f"(a = {self.__a}; b = {self.__b})"

    def getSideA(self) -> int:
        return self.__a

    def getSideB(self) -> int:
        return self.__b
    
    def area(self) -> int:
        return self.__a * self.__b
    
    def perimeter(self) -> int:
        return 2 * (self.__a + self.__b)
    
    def isSquare(self) -> bool:
        return self.__a == self.__b
    
    def replaceSides(self) -> tuple:
        temp = self.__a
        self.__a = self.__b
        self.__b = temp
        return self.__a, self.__b

class ArrayRectangles(Rectangle):
    def __init__(self, n: int, *Rectangle: list) -> None:
        self.__n = n
        self.__rectangle_array = list(Rectangle)

    def AddRectangle(self, Rectangle: Rectangle) -> bool:
        if self.__n <= 0 or len(self.__rectangle_array) >= self.__n:
            return False
        else:
            self.__rectangle_array.append(Rectangle)
            return True
    
    def __str__(self) -> str:
        return f"[{', '.join(map(str, self.__rectangle_array))}]"
        
    def NumberMaxArea(self) -> int:
        index = 0
        max = self.__rectangle_array[0].area()
        for i in range(self.__n):
            if self.__rectangle_array[i].area() > max:
                max = self.__rectangle_array[i].area()
                index = i
        return index
    
    def NumberMinPerimeter(self) -> int:
        index = 0
        min = self.__rectangle_array[0].perimeter()
        for i in range(self.__n):
            if self.__rectangle_array[i].perimeter() < min:
                min = self.__rectangle_array[i].perimeter()
                index = i
        return index
    
    def NumberSquare(self) -> list:
        squares = []
        for i in range(self.__n):
            if self.__rectangle_array[i].isSquare():
                squares.append(i)
        return squares