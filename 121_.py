class Solution(object):
    def maxProfit(self, prices):
        #compared each day witch is the highest probit.
        profit = 0
        min_price = prices[0]
        new_profit = 0
        for x in prices :
            if x < min_price:
                min_price = x
            else :
                new_profit = x - min_price
            if profit < new_profit:
                profit = new_profit
        return  profit



s = Solution()
print(s.maxProfit([2,1,2]))