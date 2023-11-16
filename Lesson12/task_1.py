class Vector:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return (((self.point2[0] - self.point1[0]) ** 2 +
                 (self.point2[1] - self.point1[1]) ** 2) ** 0.5)

    def __lt__(self, other):
        return self.length() < other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __eq__(self, other):
        return self.length() == other.length()

    # def __ne__(self, other):
    #     return self.length() != other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __ge__(self, other):
        return self.length() >= other.length()


vector1 = Vector((1, 1), (1, 10))

vector2 = Vector((1, 1), (1, 1))
print(vector1 != vector2)
