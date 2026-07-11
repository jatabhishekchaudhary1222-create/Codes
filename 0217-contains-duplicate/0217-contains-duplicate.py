class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for v in d.values():
            if v>1:
                return True
        return False
            
        