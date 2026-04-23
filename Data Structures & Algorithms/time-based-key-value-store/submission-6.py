class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # forgot that timestamp is strictly increasing, no need to check
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # get key -> list of values with timestamps
        # if timestamp given is larger than the latest timestamp, just return the latest timestamp + val
        # else search in the list to find a timestamp that is smaller than the given timestamp
        if key not in self.keys:
            return ""
        
        stack = self.keys[key]
        
        if timestamp > stack[-1][0]:
            return stack[-1][1]

        res = ""
        l, r = 0, len(stack) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if stack[mid][0] <= timestamp:
                # This is a potential candidate, move right to find a larger one
                res = stack[mid][1]
                l = mid + 1
            else:
                # Too large, move left
                r = mid - 1
                
        return res
        