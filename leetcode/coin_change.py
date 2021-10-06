from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0 : continue
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]

    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("inf")
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, 1 + sub)
            memo[n] = -1 if res == float("inf") else res
            return memo[n]
        return dp(amount)




if __name__ == '__main__':
    s = Solution()
    coins = [1]
    amount = 0
    print(s.coinChange(coins, amount))