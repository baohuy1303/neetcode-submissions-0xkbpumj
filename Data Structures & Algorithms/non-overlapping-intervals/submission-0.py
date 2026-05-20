class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # always take smaller?
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        out = 0

        for i in range(1, len(intervals)):
            last_tail = res[-1][1]

            if last_tail <= intervals[i][0]:
                res.append(intervals[i])
            else:
                out += 1
                if last_tail <= intervals[i][1]:
                    continue
                else:
                    res.pop()
                    res.append(intervals[i])
                
        return out