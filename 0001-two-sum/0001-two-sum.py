class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range (len(nums)):
            n=target-nums[i]
            if n in d:
                return [d[n],i]
            d[nums[i]]=i

        