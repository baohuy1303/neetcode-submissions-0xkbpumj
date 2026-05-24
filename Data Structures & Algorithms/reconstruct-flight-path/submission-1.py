class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # get all possible then compare?
        # edge cases: end before using all tickets?

        # adj list. sort edges/neighbors to always find smallest
        # dfs on JFK, keep going til got all tickets. if not backtrack try another path
        # guaranteed to always have correct path

        adj = { u:[] for u, v in tickets}
        tickets.sort()
        for u,v in tickets:
            adj[u].append(v)

        res = ["JFK"]

        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True

            if node not in adj or len(adj[node]) == 0:
                return False

            temp = adj[node].copy()
            for i, u in enumerate(temp):
                res.append(u)
                adj[node].pop(i)
                if dfs(u):
                    return True
                res.pop()
                adj[node].insert(i, u)
            return False

        dfs("JFK")
        return res