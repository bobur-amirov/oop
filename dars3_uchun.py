# @staticmethod bu ham classga ham obyekta tegishli
# buni classni ichida yozib quyilgan funksiya deb tushinsangiz ham buladi
# bu bizning obyektimiz ustida ish bajarmaydi
from math import sqrt, sin


class Math:
    @staticmethod
    def pow(a,b):
        return a ** b

    @staticmethod
    def abs(a):
        if a > 0:
            return a
        return -a
print(Math.pow(2,3))
print(Math.abs(-2))


class Vector:
    s = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector_len(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    @classmethod
    def vektor(cls, x, alha):
        return cls(x * sin(alha))

    def sss(self):
        return self.x + Vector.s


v = Vector(1,2)
v2 = Vector(3,5)
print(v.sss())

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_rgb(self):
        return self.r, self.g, self.b

    @classmethod
    def hex_color(cls, hex: str):
        r, g, b  = hex[:2], hex[2:4], hex[4:]
        return cls(r, g, b)

    @classmethod
    def hsl(cls, gradus, p1, p2):
        return cls(gradus, p1, p2)


color = Color(0,0,0)
print(color.get_rgb())
print(color.hex_color("1100FF"))