class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos + speed each iteration = newPos
        # group by number of iterations til target

        if len(position) == 0:
            return 0
        iterations = []
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0], reverse=True)

        for i in range(0, len(pos_speed)):
            pos = pos_speed[i][0]
            car_speed = pos_speed[i][1]
            cur_iteration = (target - pos) / car_speed
            if iterations and cur_iteration <= iterations[-1]:
                continue
            iterations.append(cur_iteration)

        return len(iterations)
