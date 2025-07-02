from src.kinds import Kinds

class Cell:
    def __init__(self, kind: Kinds, *pos):
        self.x, self.y = pos
        self.kind = kind

    def __str__(self):
        return self.kind

    def __repr__(self):
        return self.kind

    def __eq__(self, other):
        return str(self) == str(other)

    def rgb(self):
        return Kinds.rgb(self.kind)
