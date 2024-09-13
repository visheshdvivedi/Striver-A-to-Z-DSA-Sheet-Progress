/*

[5,  1,  9,  11]
[2,  4,  8,  10]
[13, 3,  6,  7]
[15, 14, 12, 16]

0, 1
0, 2
0, 3
1, 2
1, 3
2, 3

[5,  2,  13, 15]
[1,  4,  3,  14]
[9,  8,  6,  12]
[11, 10, 7,  16]

[15, 13, 2, 5]
[14, 3, 4, 1]
[12, 6, 8, 9]
[16, 7, 10, 11]

*/

#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();
        for (int i=0; i<size; i++) {
            for (int j=i+1; j<size; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (int i=0; i<size; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};