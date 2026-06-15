class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.points_list = []

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.points_list.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points_list:
            if abs(x - px) != abs(y - py) or px == x or py == y:
                continue
            res += self.points[(x, py)] * self.points[(px, y)]
        return res
