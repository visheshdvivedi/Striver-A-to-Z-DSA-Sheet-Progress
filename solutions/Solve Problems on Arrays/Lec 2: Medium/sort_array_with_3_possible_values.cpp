#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int length = nums.size();
        int red=0, white=0, blue=length-1;

        while (white <= blue)
        {
            if (nums[white] == 2) {
                swap(nums[white], nums[blue]);
                blue--;
            }
            else if (nums[white] == 1) {
                white++;
            }
            else if (nums[white] == 0) {
                swap(nums[red], nums[white]);
                red++;
                white++;
            }
        }
    }
};