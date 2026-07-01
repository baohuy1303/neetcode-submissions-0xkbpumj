''' list of strings words

CLAIM: words are sorted lexicographically by the rules of this new language.

If incorrect AND words isnt sorted? -> ""
Else return string of unique letters sorted
return ANY solution

1 <= words.length <= 100
1 <= words[i].length <= 100 
-> 10,000

a < b both needs to be true:
- the 1st differing letter is < (a comes before b)
- a is a prefix of b 

how do we represent relationships/order:
- each letter represented as a node.
- iterate thru pairs, 1st differing letter would get recorded as a directed
graph

how do we return the result back starting from the smallest node?
- test from every node?


 ''' 
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w} # letter: [letters]
        dep = {c: 0 for c in adj_list} # letter: num_of_dep

        if len(words) == 0:
            return ""
        if len(words) == 1:
            return words[0]

        p1 = 0
        p2 = 1

        while p2 < len(words):
            w1 = words[p1]
            w2 = words[p2]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    continue
                if c2 in adj_list[c1]:
                    break
                adj_list[c1].add(c2)
                dep[c2] += 1
                break

            p1 += 1
            p2 += 1

        q = deque()
        for letter, num_of_dep in dep.items():
            if num_of_dep == 0:
                q.append(letter)
        res = ""
        while q:
            letter = q.popleft()
            res += letter
            for c in adj_list[letter]:
                dep[c] -= 1
                if dep[c] == 0:
                    q.append(c)

        if len(res) < len(dep):
            return ""
        return res
            

        









