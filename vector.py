from math import sqrt
from math import acos


class vector(object):
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except (ValueError, TypeError) as e:
            print("Co-Ordinates need to be LIST and non-empty")


    def __str__(self):
        return "Vector: {p}".format(p=self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def add(self, v):
        return tuple(round(self.coordinates[_] + v.coordinates[_], 3) for _ in range(self.dimension))


    def sub(self, v):
        return tuple(round(self.coordinates[_] - v.coordinates[_], 3) for _ in range(self.dimension))


    def scalar_mul(self, s):
        return tuple(round(self.coordinates[_] * s, 3) for _ in range(self.dimension))


    def magnitude(self):
        return round(sqrt(sum([_**2 for _ in self.coordinates])), 3)


    def normalize(self):
        # Previous Version: return tuple(round(( _ / self.magnitude()), 3) for _ in self.coordinates)
        return self.scalar_mul(1.0 / self.magnitude())  # re-using existing code increases efficiency.


    def dot_product(self, v):
        return round(sum([self.coordinates[_] * v.coordinates[_] for _ in range(self.dimension)]),3)


    def angle(self, v):
        return round(acos(self.dot_product(v) / (self.magnitude() * v.magnitude())), 3)
