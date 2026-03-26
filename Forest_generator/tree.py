import random

class Tree:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.levels = []

    def grow(self):
        if self.height == 0:
            self.levels.append("|")
        elif self.height == 1:
            self.levels[0] += "|"
            self.levels.append("/\\")
        elif self.height == 2:
            self.levels.insert(1, "//\\\\")
        else:
            prev_leaf_count = len(self.levels[1]) // 2
            leaf_count = prev_leaf_count + random.randint(0, 1)
            level = ("/" * leaf_count) + ("\\" * leaf_count)
            self.levels.insert(1, level)
        self.height += 1

    def coordinates(self):
        coor = {}
        for y, level in enumerate(self.levels):
            x0 = -len(level) // 2 + 1
            for x, char in enumerate(level):
                coor[(x0 + x, -y)] = char
        return coor

    def __str__(self):
        result = ""
        for level in reversed(self.levels):
            padding = self.height - len(level) // 2
            result += " " * padding + level + "\n"
        return result
