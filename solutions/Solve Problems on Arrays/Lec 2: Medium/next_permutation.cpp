#include <vector>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {

        // find pivot
        int pivot = -1, length = nums.size();
        for (int i = length - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                pivot = i;
                break;
            }
        }
        // if pivot is not found, simply sort the array and return
        if (pivot == -1) {
            sort(nums.begin(), nums.end());
            return;
        }

        // find next number to switch from
        int next = -1;
        for (int i = length - 1; i >= 0; i--) {
            if (nums[i] > nums[pivot]) {
                next = i;
                break;
            }
        }   

        // swap the next and pivot
        swap(nums[pivot], nums[next]);

        // sort array from pivot+1 to end
        sort(nums.begin() + pivot + 1, nums.end());
    }
};