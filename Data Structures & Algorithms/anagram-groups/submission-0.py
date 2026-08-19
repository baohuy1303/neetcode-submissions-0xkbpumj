class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        word_dict = defaultdict(list)
        for word in strs:
            freq_arr = [0] * 26
            for c in word:
                freq_arr[ord(c) - ord('a')] += 1

            word_dict[tuple(freq_arr)].append(word)

        for words in word_dict.values():
            res.append(words)
        return res