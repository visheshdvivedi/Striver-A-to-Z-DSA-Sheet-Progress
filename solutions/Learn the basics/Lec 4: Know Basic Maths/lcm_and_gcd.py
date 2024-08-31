class Solution:
    def getGCD(self, a, b):
        if b == 0: return a
        return self.getGCD(b, a % b)
        
    def lcmAndGcd(self, a, b):
        gcd = self.getGCD(a, b)
        lcm = (a * b) // gcd
        return [lcm, gcd]