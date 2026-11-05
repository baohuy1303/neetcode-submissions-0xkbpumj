class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        cur_start, cur_end = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= cur_end:
                cur_end = max(cur_end, e)
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = s, e

        res.append([cur_start, cur_end])
        return res