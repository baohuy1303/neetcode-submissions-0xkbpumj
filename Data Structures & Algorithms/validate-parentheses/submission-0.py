class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in p_map:
                stack.append(c)
                continue

            if len(stack) > 0:
                if p_map[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False