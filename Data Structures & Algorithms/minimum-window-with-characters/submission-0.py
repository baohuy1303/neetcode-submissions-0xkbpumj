class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        total_t_freq = len(t_map)

        if total_t_freq == 0:
            return ""
        
        l, r = 0, 0
        total_s_freq = 0
        s_map = defaultdict(int)

        res = [-1, -1, float('inf')]

        for r in range(0, len(s)):
            cur = s[r]
            s_map[cur] += 1
            if cur in t_map and s_map[cur] == t_map[cur]:
                total_s_freq += 1
                
            while total_s_freq == total_t_freq and l < len(s):
                if r-l+1 < res[2]:
                    res = [l, r, r-l+1]
                
                l_char = s[l]
                s_map[l_char] -= 1
                if l_char in t_map and s_map[l_char] < t_map[l_char]:
                    total_s_freq -= 1
                l += 1

        return s[res[0]:res[1]+1] if res[0] != -1 else ""