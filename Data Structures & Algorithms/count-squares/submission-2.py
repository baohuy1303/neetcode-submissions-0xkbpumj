''' stream of points

add([x,y]): Duplicate points are allowed, treated as separate points

count([x, y]): number of unique ways to form a square, starting from point [x, y]

from point given, we need to find all unique ways to form a square
all sides are equal. only 3 additional points. no diagonal.

how do we form a square?
    - start from point, and pick 1 dir to go, and keep turning until we find ourselves (found a cycle)
    how do we know where to turn at a point tho?
    
    - we go up-left, up-right, bottom-right, bottom-left starting from point.
    and we amplify the unit (so first we travel by 1, next by 2 and so on to check)

how to still count duplicates?
    - we have dict [x, y] is key, and the remaining times we can start our search from [x, y]

0 <= x, y <= 1000
 '''
class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        dir = [
            [(0, 1), (1, 0), (0, -1)],
            [(1, 0), (0, -1), (-1, 0)],
            [(0, -1), (-1, 0), (0, 1)], 
            [(-1, 0), (0, 1), (1, 0)]
            ]

        res = 0
        for multiplier in range(1, 1001):
            for d in dir:
                valid = True
                x = point[0]
                y = point[1]
                current_square_counts = []
                for nx, ny in d:
                    x = x + nx * multiplier
                    y = y + ny * multiplier
                    if x < 0 or y < 0 or x > 1000 or y > 1000 or (x, y) not in self.points:
                        valid = False
                        break
                    current_square_counts.append(self.points[(x, y)])

                if valid:
                    res += current_square_counts[0] * current_square_counts[1] * current_square_counts[2]

        return res
            


