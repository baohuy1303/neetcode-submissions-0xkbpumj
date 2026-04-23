class TimeMap:

    def __init__(self):
        self.keys = {}

    def binary_search(self, stack, timestamp):
        # need to find timestamp that's smaller than given timestamp, but latest/largest out of the rest
        l = 0
        r = len(stack) - 1
        while l <= r:
            mid = (r + l) // 2
            mid_time = stack[mid][0]
            if mid_time == timestamp:
                print(mid, 99)
                return (mid, 1)
            elif mid_time < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return (l, 0)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # binary search to find the place to insert
        tuple_time_val = (timestamp, value)
        if key not in self.keys:
            self.keys[key] = [tuple_time_val]
            return
        stack = self.keys[key]
        if len(stack) == 1:
            if stack[-1][0] <= timestamp:
                stack.append(tuple_time_val)
                return
            stack.insert(0, tuple_time_val)
            return

        insertion = self.binary_search(stack, timestamp)[0]
        stack.insert(insertion, tuple_time_val)
        return

    def get(self, key: str, timestamp: int) -> str:
        # get key -> list of values with timestamps
        # if timestamp given is larger than the latest timestamp, just return the latest timestamp + val
        # else search in the list to find a timestamp that is smaller than the given timestamp
        if key not in self.keys:
            return ""
        
        stack = self.keys[key]
        
        if timestamp > stack[-1][0]:
            return stack[-1][1]

        index_tuple = self.binary_search(stack, timestamp)
        index = 0
        if index_tuple[1] == 0:
            index = max(index_tuple[0] - 1, 0)
        else:
            index = index_tuple[0]
        if stack[index][0] > timestamp:
            return ""
        return stack[index][1]
        