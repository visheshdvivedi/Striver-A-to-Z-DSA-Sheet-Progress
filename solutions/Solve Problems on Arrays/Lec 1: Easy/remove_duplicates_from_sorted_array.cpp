#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       int size = 1;
       for (int i=1; i<nums.size(); i++)
       {
            if (nums[i] != nums[i-1]) {
                nums[size] = nums[i];
                size++;
            }
       }
       return size;
    }
};