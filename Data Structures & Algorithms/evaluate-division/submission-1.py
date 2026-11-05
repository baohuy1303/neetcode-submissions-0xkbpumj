class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(src, dst, prod, seen):
            if src == dst:
                return prod

            seen.add(src)
            for neighbor, weight in graph[src]:
                if neighbor in seen:
                    continue

                res = dfs(neighbor, dst, prod * weight, seen)
                if res != -1:
                    return res
            return -1

        res = []
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(u, v, 1.0, set()))

        return res