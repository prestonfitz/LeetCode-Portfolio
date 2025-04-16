class Solution:
    def fib(self, n: int, memo = [0,1]) -> int:
        if n < len(memo):
            return memo[n]
        if len(memo) >= n:
            return (memo[-1] + memo[-2])
        else:
            memo.append(memo[-1] + memo[-2])
            return self.fib(n, memo)