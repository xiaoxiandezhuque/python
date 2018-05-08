
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ReplacePoint(object):
    def __init__(self, color, fromPoint, toPoint):
        self.color = color
        self.fromPoint = fromPoint
        self.toPoint = toPoint






if __name__ == "__main__":
    a = Point(1, 1)
    b = Point(2, 3)
    c = ReplacePoint(3, "a", a, b)
    print(c.num)
