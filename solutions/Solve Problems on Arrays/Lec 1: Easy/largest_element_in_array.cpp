#include <vector>

using namespace std;

class Solution {
  public:
    int largest(vector<int> &arr) {
        int maxElement = arr[0];
        for (int i=0; i<arr.size(); i++) {
            maxElement = max(maxElement, arr[i]);
        }
        return maxElement;
    }
};