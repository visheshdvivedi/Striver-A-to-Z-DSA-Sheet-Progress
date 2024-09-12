#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> leaders(int n, int arr[]) {
        int maxleader = arr[n-1];
        
        vector<int> out;
        out.push_back(maxleader);
        
        for (int i=n-2; i>=0; i--) {
            if (arr[i] >= maxleader) {
                maxleader = max(maxleader, arr[i]);
                out.push_back(arr[i]);
            }
        }
        
        reverse(out.begin(), out.end());
        return out;
    }
};