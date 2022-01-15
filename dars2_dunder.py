class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x1 = self.x + other.x
        self.y1 = self.y + other.y
        return f"{self.x1} {self.y1}"

    def __sub__(self, other):
        self.x2 = self.x - other.x
        self.y2 = self.y - other.y
        return f"{self.x2} {self.y2}"


A = Vector(5, 6)
B = Vector(5, 2)
print(A + B)
print(A - B)
