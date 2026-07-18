''' strs[i] contains any possible characters out of 256 valid ASCII characters.

how to treat item separation?
    - len of item + "#" + encoded item
 '''

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += (str(len(s)) + "#" + s)
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            temp = i
            while i < len(s) and s[i] != "#":
                i += 1
            length = int(s[temp:i]) + 1
            decoded.append(s[i+1:i+length])
            i += length
        
        return decoded
