class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            countChar = 0
            for c in word:
                countChar += 1
            msg += str(countChar) + "#" + word
        print(msg)
        return msg
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        lastChar = -1
        i = 0
        while i < len(s):
            if s[i] == "#" and i > lastChar:
                j = i - 1
                while j > lastChar and s[j].isdigit():
                    j -= 1
                skip = int(s[j+1:i] if len(s[j+1:i]) > 0 else 0)
                i += skip
                res.append(s[i-skip+1 : i+1])
                lastChar = i
            i += 1

        return res


        