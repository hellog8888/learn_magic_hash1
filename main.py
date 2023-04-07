class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __eq__(self, other):
        if isinstance(other, Rect):
            return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.width, self.height))