#include <vector>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        int actual = 0;
        int expected = (length * (length+1))/2;

        for (int i=0; i<length; i++)
            actual += nums[i];

        return expected - actual;
    }
};