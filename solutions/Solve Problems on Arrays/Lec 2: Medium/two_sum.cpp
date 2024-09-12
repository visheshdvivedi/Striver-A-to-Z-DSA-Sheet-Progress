#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffs;
        vector<int> out(2);

        for (int i=0; i<nums.size(); i++)
        {
            if (diffs.find(nums[i]) != diffs.end())
            {
                out[0] = diffs[nums[i]];
                out[1] = i;
                return out;
            }
            else
                diffs[target - nums[i]] = i;
        }
        return out;
    }
};