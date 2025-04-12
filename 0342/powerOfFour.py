class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or int(n) != n:
            return False
        elif n == 4 or n == 1:
            return True
        else:
            return self.isPowerOfFour(n/4)
        