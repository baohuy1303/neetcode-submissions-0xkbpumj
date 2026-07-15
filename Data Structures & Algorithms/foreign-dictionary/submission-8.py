''' return str of unique letters sorted lexi increasing order


"a" "b"
1st letter differ: a < b
a is a prefix of b (a cant be longer than b if matches)

represent relationships as a graph
each letter is a node that points to the smaller char
if there is a cycle then the dict is invalid

use a visited and visiting dfs cycle detection
if a node has no smaller char, means its the smallest and we can start appending to our result
mark as visited.

how to get the nodes? 
to extract the nodes and relationship have two pointers at a pair:
    - go letter by letter on each only stop when theres a differing letter
    - check if p1 exists but p2 doesnt, this means its a longer prefix -> invalid, return ""
    else:
    - record that relationship and move to the next pair

O(n*t) to record relationship, n: is number of words, t: max letters

 '''
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = defaultdict(set) # letter: [list of smaller letters]

        if len(words) <= 1:
            return words[0]

        for word in words:
            for c in word:
                adj_list[c]

        p1, p2 = 0, 1
        while p2 < len(words):
            w1 = words[p1]
            w2 = words[p2]

            for i in range(len(w1)):
                if i >= len(w2):
                    return ""
                c1 = w1[i]
                c2 = w2[i]
                if c1 == c2:
                    continue
                adj_list[c2].add(c1)
                break
            p1 += 1
            p2 += 1

        res = [""]
        visited = set()
        def dfs(c, visiting):
            if c in visited:
                return True
            if c in visiting:
                return False

            visiting.add(c)
            for letter in adj_list[c]:
                if not dfs(letter, visiting):
                    return False

            visiting.remove(c)
            visited.add(c)
            res[0] += c
            return True

        for c in adj_list:
            if not dfs(c, set()):
                return ""
        return res[0]
                        
