#include <unordered_map>

using namespace std;

class Solution{
    public:
    int lenOfLongSubarr(int A[],  int N, int K) 
    {
        int sum = 0;
        int maxlength = 0;
        unordered_map<int, int> prefixsum;
        
        for (int i=0; i<N; i++) {
            sum += A[i];
            if (sum == K) 
                maxlength = max(maxlength, i+1);
            if (prefixsum.find(sum - K) != prefixsum.end())
                maxlength = max(maxlength, i - prefixsum[sum - K]);
            if (prefixsum.find(sum) == prefixsum.end())
                prefixsum[sum] = i;
        }
        return maxlength;
    } 

};