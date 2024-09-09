#include <vector>

using namespace std;

class Solution{
    public:
    vector<int> findUnion(int arr1[], int arr2[], int n, int m)
    {
        vector<int> out;
        int firstptr = 0, secondptr = 0;
        
        while (firstptr < n && secondptr < m)
        {
            if (arr1[firstptr] == arr2[secondptr]) {
                out.push_back(arr1[firstptr]);
                firstptr++;
                secondptr++;
                
                while (firstptr < n && arr1[firstptr] == arr1[firstptr-1])
                    firstptr++;
                    
                while (secondptr < m && arr2[secondptr] == arr2[secondptr-1])
                    secondptr++;
                
            }
            else if (arr1[firstptr] < arr2[secondptr]) {
                out.push_back(arr1[firstptr]);
                firstptr++;
                
                while (firstptr < n && arr1[firstptr] == arr1[firstptr-1])
                    firstptr++;
            }
            else {
                out.push_back(arr2[secondptr]);
                secondptr++;
                    
                while (secondptr < m && arr2[secondptr] == arr2[secondptr-1])
                    secondptr++;
            }
            
        }
        
        while (firstptr < n) {
            if (firstptr > 0 && arr1[firstptr] != arr1[firstptr-1])
                out.push_back(arr1[firstptr]);
            firstptr++;
        }
            
        while (secondptr < m){
            if (secondptr > 0 && arr2[secondptr] != arr2[secondptr-1])
                out.push_back(arr2[secondptr]);
            secondptr++;
        }
        
        return out;
    }
};