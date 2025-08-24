"""
Link: https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number
Name: Count all digits of a number
Difficulty: Easy
Description:
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
"""

class Solution:
    def countDigit(self, n):
        return len(str(n))