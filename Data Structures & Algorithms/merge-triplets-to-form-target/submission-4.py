class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute: apply trip[i] with all the other trip O(2n)
        # we always try to hit target
        # triplet that have a number > target, we skip

        ''' new_list = []
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            new_list.append([a,b,c])

        if len(new_list) == 0:
            return False
        if len(new_list) == 1:
            if new_list[-1] == target:
                return True
            return False

        for i in range(len(new_list) - 1):
            n1 = new_list[i]
            n2 = new_list[i+1]

            new = [max(n1[0], n2[0]), max(n1[1], n2[1]), max(n1[2], n2[2])]
            new_list[i+1] = new

        if new_list[-1] == target:
            return True
        return False '''

        # spacemaxxing, this 1 O(1) instead of O(n) 
        current_max = [0, 0, 0]
        
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                current_max[0] = max(current_max[0], a)
                current_max[1] = max(current_max[1], b)
                current_max[2] = max(current_max[2], c)
                
        return current_max == target


