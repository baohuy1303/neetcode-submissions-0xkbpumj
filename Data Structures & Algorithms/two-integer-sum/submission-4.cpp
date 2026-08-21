class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (lookup.contains(diff)) {
                return {lookup[diff], i};
            }
            
            lookup[nums[i]] = i;
        }
        
        return {};
    }
};
