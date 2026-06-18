''' return all elements up until kth position

1 <= nums.length <= 10^4 -> O(n)

count the freqs into a dict

sort the freq and get the top k elements -> O(nlogn)

heapify -> O(n)
pop() -> O(logn)

Worst time: O(klogn)

bucket list/sort:
    - initialize an array of n(len(nums)) (worst case: freq == n)
    - freq of each number into a bucket ie. freq = index of the array, and the value would be the number
    - iterate from -1 til 0 until we have k elemnts
    
same freq?
    - 
-> O(n)
 '''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums)+2)]

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num, freq in freq.items():
            arr[freq].append(num)

        res = []
        for i in range(len(arr) - 1, -1, -1):
            while len(arr[i]) != 0:
                if len(res) == k:
                    return res
                if arr[i]:
                    res.append(arr[i][-1])
                arr[i].pop()

        return res


