#include <vector>

using namespace std;

class Solution
{
public:
    bool check(vector<int> &nums)
    {
        int count = 0;
        int length = nums.size();
        for (int i = 0; i < length; i++)
        {
            if (nums[i] > nums[(i + 1) % length])
                count++;
        }
        return count <= 1;
    }
};