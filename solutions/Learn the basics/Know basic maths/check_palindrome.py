"""
Link: https://takeuforward.org/plus/dsa/problems/palindrome-number
Name: Palindrome Number
Difficulty: Easy
Description:
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]