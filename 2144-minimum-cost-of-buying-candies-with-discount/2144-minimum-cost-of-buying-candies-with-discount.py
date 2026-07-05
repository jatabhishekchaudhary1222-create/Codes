class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a=0
        cost.sort()
        cost=cost[::-1]
        for i in range(len(cost)):
            if i%3!=2:
                a+=cost[i]
            elif i%3==2:
                pass
        return a
        