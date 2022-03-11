class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle():

    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def area(self):
        return abs((self.point1.x * (self.point2.y - self.point3.y) + 
                    self.point2.x * (self.point3.y - self.point1.y) + 
                    self.point3.x * (self.point1.y - self.point2.y)) / 2.0)
    
    def is_point_inside(self, point):

        triangle_1 = Triangle(point, self.point2, self.point3)
        triangle_2 = Triangle(self.point1, point, self.point3)
        triangle_3 = Triangle(self.point1, self.point2, point)

        return self.area() == triangle_1.area() + triangle_2.area() + triangle_3.area()

point = Point(0.5,0.5)
triangle = Triangle(Point(0, 0), Point(-1, 1), Point(1, 1))
print(triangle.is_point_inside(point))