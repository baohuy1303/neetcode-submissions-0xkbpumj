class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # build a dict to know where the furthest char is at
        # during cur window, if found a larger dist, update it to keep going
        # if at end, append and start new cycle

        dist = {}
        for i in range(len(s)):
            dist[s[i]] = max(i, dist.get(s[i], i))
            
        cur = 0
        furthest = 0
        res = []
        for i in range(len(s)):
            cur += 1
            furthest = max(furthest, dist[s[i]])
            if furthest == i:
                res.append(cur)
                cur = 0
        return res