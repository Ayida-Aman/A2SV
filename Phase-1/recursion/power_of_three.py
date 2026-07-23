class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <1:
            return False
        def helper(n):
            while n % 3 == 0 and n>1:
                n = n//3
            if n == 1:
                return True
            return False
        return helper(n)
        
        