class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        if len(intervals) == 1:
            return 0
        cur_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < cur_end:
                if end >= cur_end:
                    res += 1
                    continue
                else:
                    cur_end = end
                    res += 1
            else:
                cur_end = end

        return res