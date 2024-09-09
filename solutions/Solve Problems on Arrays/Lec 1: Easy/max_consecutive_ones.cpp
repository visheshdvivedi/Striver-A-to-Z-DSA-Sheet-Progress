#include <vector>

using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxVal = 0;
        int currVal = 0;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i] == 1)
                currVal++;
            else {
                maxVal = max(maxVal, currVal);
                currVal = 0;
            }
        }
        return max(maxVal, currVal);
    }
};