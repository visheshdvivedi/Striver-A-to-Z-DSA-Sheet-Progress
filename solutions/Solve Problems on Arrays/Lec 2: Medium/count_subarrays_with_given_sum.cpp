#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> summap;
        summap[0] = 1;

        int count = 0;
        int presum = 0;

        for (int i=0; i<nums.size(); i++) {
            presum += nums[i];
            int diff = presum - k;
            count += summap[diff];
            summap[presum] += 1;
        }

        return count;
    }
};