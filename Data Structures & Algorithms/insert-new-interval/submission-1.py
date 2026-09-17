class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_s, new_e = newInterval

        for i in range(len(intervals)):
            s, e = intervals[i]
            
            if new_e < s:
                res.append([new_s, new_e])
                return res + intervals[i:]
            elif e < new_s:
                res.append([s, e])
            else:
                new_s = min(s, new_s)
                new_e = max(e, new_e)
        res.append([new_s, new_e])
        return res