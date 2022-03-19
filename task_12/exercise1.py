import math

class Circle():
    Min_R = 0

    def __init__(self, r: int=5) -> None:
        self.__r = r
    
    @property
    def radius(self) -> int:
        return self.__r

    @radius.setter
    def radius(self, r: int) -> None:
        if r < self.Min_R:
            raise ValueError("Negative radius is not possible")
        self.__r = r

    def __str__(self) -> str:
        return f"The circle radius is {self.__r}"
    
    def area(self) -> float:
        return math.pi * pow(self.__r, 2)
    
    def increase(self, n: int) -> int:
        return n * self.__r
    
    @staticmethod
    def isBig(radius: int) -> bool:
        return radius > 100
    
    def __add__(self, other):
        return Circle(self.__r + other.__r)
    
    def __sub__(self, other):
        return Circle(self.__r - other.__r)

class Ring(Circle):
    def __init__(self, rin: int=2) -> None:
        self.__rin = rin
    
    @property
    def ring(self) -> int:
        return self.__rin
    
    @ring.setter
    def ring(self, rin: int) -> None:
        if rin < self.Min_R or rin > self.radius:
            raise ValueError("Such ring radius is not possible")
        self.__rin = rin
    
    def __str__(self) -> str:
        return f"The ring radius is {self.__rin}"
    
    def area(self, circle: Circle) -> float:
        return math.pi * (pow(circle.radius, 2) - pow(self.__rin, 2))
    
    def increase(self, n: int) -> int:
        return n * self.__rin