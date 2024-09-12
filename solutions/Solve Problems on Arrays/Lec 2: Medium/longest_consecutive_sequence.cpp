#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 1, length = nums.size();
        unordered_set numset(nums.begin(), nums.end());

        if (length == 0) return 0;

        for (int i=0; i<length; i++) {
            // check if nums[i] can be a valid starting point
            if (numset.find(nums[i]-1) == numset.end()) {
                int seqcount = 1;
                while (numset.find(nums[i] + seqcount) != numset.end()) 
                    seqcount++;
                
                // set longest
                longest = max(longest, seqcount);
            }
        }

        return longest;
    }
};