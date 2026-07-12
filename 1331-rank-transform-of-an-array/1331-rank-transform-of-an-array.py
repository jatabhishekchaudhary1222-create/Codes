class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        a=sorted(set(arr))
        d={}
        for i,num in enumerate(a):
            d[num]=i+1
        ans=[]
        for num in arr:
            ans.append(d[num])
        return ans