class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp=0
        mi=prices[0]
        for i in prices:
            if i<mi:
                mi=i
            p=i-mi
            if p>mp:
             mp=p
        return mp
        