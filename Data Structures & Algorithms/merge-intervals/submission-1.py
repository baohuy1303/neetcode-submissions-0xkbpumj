class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        cur_interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if cur_interval[1] < intervals[i][0]:
                res.append(cur_interval)
                cur_interval = intervals[i]
            elif cur_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                cur_interval = [min(cur_interval[0], intervals[i][0]), max(cur_interval[1], intervals[i][1])]

        res.append(cur_interval)
        return res