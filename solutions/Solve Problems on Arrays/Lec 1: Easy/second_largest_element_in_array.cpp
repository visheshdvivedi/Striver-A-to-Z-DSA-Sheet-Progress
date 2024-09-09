#include <vector>

using namespace std;

class Solution {
  public:
    int print2largest(vector<int> &arr) {
        int largest = max(arr[0], arr[1]);
        int second = min(arr[0], arr[1]);
        
        for (int i=2; i<arr.size(); i++)
        {
            if (arr[i] > largest) {
                second = largest;
                largest = arr[i];
            }
            else if (arr[i] > second && arr[i] < largest)
            {
                second = arr[i];
            }
        }
        
        if (largest == second) return -1;
        return second;
    }
};