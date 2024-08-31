class Solution:
    def armstrongNumber (self, n):
        cubes_sum = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            cubes_sum += pow(digit, 3)
            temp //= 10
        if cubes_sum == n: return "true"
        else: return "false"