#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int index = -1, buy = INT_MAX, maxprofit = 0;
        int length = prices.size();
        for (int i=0; i<length; i++)
        {
            if (i != length-1 && prices[i] < prices[i+1] && prices[i] < buy) {
                index = i;
                buy = prices[i];
            }
            else {
                int profit = prices[i] - buy;
                maxprofit = max(maxprofit, profit);
            }
        }
        return maxprofit;
    }
};