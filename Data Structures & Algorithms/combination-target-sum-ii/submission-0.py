class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' contraints:
        each element can be only be in the combination once
        no duplicate combination

        # how do we make sure the combination is unique
        - decide i or no i
        - then at i decide i+1 or no i+1
        ...
        this make sures each element in combination once

        # sort the array, go thru each index
        # skip index with same val
        this gives no duplicate combination
        '''
        candidates.sort()
        res = []
        def dfs(index, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or index >= len(candidates):
                return
            
            cur_num = candidates[index]
            # keep current number branch
            path.append(cur_num)
            dfs(index + 1, path, total + cur_num)
            path.pop()

            # determine skip
            next_i = index + 1
            while next_i < len(candidates) and cur_num == candidates[next_i]:
                next_i += 1

            # skip and go to next
            dfs(next_i, path, total)
            return
        
        dfs(0, [], 0)
        return res
