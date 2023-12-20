class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices = sorted(prices)
        cost = prices[0] + prices[1]
        result = money - cost
        if result<0:
            return money
        else:
            return result
        