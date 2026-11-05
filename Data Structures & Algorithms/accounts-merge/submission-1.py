from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graphs = defaultdict(list)
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            first = acc[1]
            email_to_name[first] = name

            for email in acc[1:]:
                graphs[first].append(email)
                graphs[email].append(first)
                email_to_name[email] = name

        seen = set()
        def dfs(email, group):
            seen.add(email)
            group.append(email)
            for nei in graphs[email]:
                if nei not in seen:
                    dfs(nei, group)
            return
        
        res = []
        for email in email_to_name:
            if email not in seen:
                groups = []
                dfs(email, groups)
                res.append([email_to_name[email]] + sorted(groups))

        return res


