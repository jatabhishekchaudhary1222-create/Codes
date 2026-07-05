class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        l=0
        t=sum(nums)
        for i in range(len(nums)):
            r=t-l-nums[i]
            ans.append(abs(l-r))
            l+=nums[i]
        return ans