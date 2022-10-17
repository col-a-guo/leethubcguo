# memoize ways for low n
# to find n:
# you can take n-1 and add a 1 to the front
# or an n-2 and add a 2 to the front
# so this is just fibbonaci 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = []
        for i in range(n):
            memo.append(self.climb_memo(memo, i))
        return memo[n-1]
    def climb_memo(self, memo, i: int) -> int:
        #i goes up to n-1
        if i == 0:
            return 1
        if i == 1:
            return 2
        else:
            return memo[i-2]+memo[i-1]