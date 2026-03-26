class Forest:
    def __init__(self, cols, rows):
        self.columns = cols
        self.rows = rows
        self.inhabitants = []
        self.soil = [[" " for _ in range(self.columns)] for _ in range(self.rows)]

    def place(self, obj, x, y):
        if x < 0 or x >= self.columns or y < 0 or y >= self.rows:
            return

        obj.x, obj.y = x, y
        my_z_index = y * self.columns + x

        i = 0
        placed = False
        while i < len(self.inhabitants) and not placed:
            other = self.inhabitants[i]
            z_index = other.y * self.columns + other.x
            if my_z_index < z_index:
                self.inhabitants.insert(i, obj)
                placed = True
            i += 1

        if not placed:
            self.inhabitants.append(obj)

    def grow(self):
        for inhabitant in self.inhabitants:
            inhabitant.grow()

    def __str__(self):
        # Reset soil
        self.soil = [[" " for _ in range(self.columns)] for _ in range(self.rows)]

        for inhabitant in self.inhabitants:
            x0 = inhabitant.x
            y0 = inhabitant.y
            for (dx, dy), char in inhabitant.coordinates().items():
                x = x0 + dx
                y = y0 + dy
                if 0 <= x < self.columns and 0 <= y < self.rows:
                    self.soil[y][x] = char

        return "\n".join("".join(row) for row in self.soil)
