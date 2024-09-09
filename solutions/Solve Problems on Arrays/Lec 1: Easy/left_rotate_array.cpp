#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int length = nums.size();
        
        if (k == 0) return;
        else if (k >= length)
            k %= length;

        reverse(nums.begin(), nums.end() - k);
        reverse(nums.begin() + (length - k), nums.end());
        reverse(nums.begin(), nums.end());
    }
};