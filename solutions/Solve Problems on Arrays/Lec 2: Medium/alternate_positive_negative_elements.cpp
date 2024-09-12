#include <vector>

using namespace std;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int length = nums.size();
        int evenptr = 0, oddptr = 1;
        vector<int> out(length);

        for (int i=0; i<length; i++) {
            if (nums[i] > 0) {
                out[evenptr] = nums[i];
                evenptr += 2;
            }
            else {
                out[oddptr] = nums[i];
                oddptr += 2;
            }
        }
        return out;
    }
};