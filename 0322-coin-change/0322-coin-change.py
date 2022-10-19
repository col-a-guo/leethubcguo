#questions
#negative coins (i.e. change) isn't allowed, right?
#
#general idea
#we are essentially transversing a large graph with a sink and implied edges
#so use a shortest path algorithm
#memoize, add lowest, build up and check each coin for prior options
#figure out LCM for coin pairs?
#
#
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        memo = [10000000 for i in range(amount+1)]
        i = 0
        while i < len(coins):
            if coins[i] <= amount:
                memo[coins[i]] = 1
                i += 1
            else:
                coins.pop(i)
        
                
        if coins == []:
            return -1
        for i in range(min(coins)+1, amount+1):
            memo[i] = self.coinChangeMemo(memo, coins, i)
           
        if memo[amount] == 10000000:
            return -1
        else:
            return memo[amount]
        
    def coinChangeMemo(self, memo, coins, index):
        best = memo[index]
        for coin in coins:
            if index >= coin:
                guess = memo[index-coin]
                if guess < best:
                    best = guess+1
        return best
                