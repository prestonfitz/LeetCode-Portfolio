class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0 or (type(n) == float and not int(n) == n):
            return False
        elif n <= 2 and n > 0:
            return True
        else:
            return self.isPowerOfTwo(n/2)