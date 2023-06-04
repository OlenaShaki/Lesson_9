class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area (self):
        return (self.width * self.length /2)
l = Parallelogram(5, 6)
print(l.get_area())

class Square (Parallelogram):
    def __init__(self, width):
        super().__init__(width, width)

    def get_area (self):
        super().get_area()
        return (self.width **2)

p = Square(5)
print(p.get_area())