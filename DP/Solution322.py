class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        m = amount
        # dp[i]
        min_coin = min(coins)
        dp = [10  ** 8 for _ in range(m + 1)]
        dp[0] = 0
        for i in range(1, m + 1):
            if i < min_coin:
                dp[i] = -1
                continue
            for coin in coins:
                if i - coin >= 0:
                    if dp[i - coin] != -1:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
            if dp[i] == 10 ** 8:
                dp[i] = -1
        return dp[m]
s = Solution()
print(s.coinChange( [3,4,5], 8))