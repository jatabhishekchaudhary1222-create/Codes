class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new=sorted(set(arr))
        d={}
        for i,k in enumerate(new):
            d[k]=i+1
        ans=[]
        for i in arr:
            ans.append(d[i])
        return ans

            