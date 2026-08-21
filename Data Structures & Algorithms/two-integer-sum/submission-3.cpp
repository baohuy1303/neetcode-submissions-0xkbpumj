class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        int i = 0;
        for (auto num: nums){
            if(lookup.contains(target-num)){
                return vector{lookup[target-num], i};
            }
            lookup[num] = i;
            i++;
        }
        return vector{0, 0};
    }
};
