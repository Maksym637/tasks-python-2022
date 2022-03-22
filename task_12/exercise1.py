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
        if r < 0:
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
    def __init__(self, inner_radius: int=2) -> None:
        self.__inner_radius = inner_radius
    
    @property
    def ring(self) -> int:
        return self.__inner_radius
    
    @ring.setter
    def ring(self, inner_radius: int) -> None:
        if inner_radius < self.Min_R or inner_radius > self.radius:
            raise ValueError("Such ring radius is not possible")
        self.__inner_radius = inner_radius
    
    def __str__(self) -> str:
        return f"The ring radius is {self.__inner_radius}"
    
    def area(self, circle: Circle) -> float:
        return math.pi * (pow(circle.radius, 2) - pow(self.__inner_radius, 2))
    
    def increase(self, n: int) -> int:
        return n * self.__inner_radius