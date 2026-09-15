class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur_start, cur_end = intervals[0]
        res = []
        for new_start, new_end in intervals:
            if new_start > cur_end:
                res.append([cur_start, cur_end])
                cur_start, cur_end = new_start, new_end
            else:
                cur_end = max(new_end, cur_end)
        res.append([cur_start, cur_end])
        return res