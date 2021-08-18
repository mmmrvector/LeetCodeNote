class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i]表示第 i + 1天的最大收益
        dp = [ 0 ] * len(prices)
        # cost[i] 表示前 i + 1天内最后一次操作为买入的最大收益
        # cost[i]可以用单个变量代替，为方便理解，采用数组表示
        cost = [ -1 * x for x in prices ]
        for i in range(0, len(prices)):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = max(0, prices[1] - prices[0])
                cost[i] = max(cost[i], cost[i - 1])
            elif i == 2:
                dp[i] = max(0, prices[2] - prices[1], prices[2] - prices[0], prices[1] - prices[0])
                cost[i] = max(cost[:3])
            else:
                dp[i] = max(prices[i] + cost[i - 1], dp[i - 1])
                cost[i] = max(cost[i - 1], dp[i - 2] + cost[i])
        return dp[len(prices) - 1]
s = Solution()
print(s.maxProfit([1,2,3,0,2]))