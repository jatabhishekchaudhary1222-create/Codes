class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]<nums[a]:
                a=i
            if nums[i]>nums[b]:
                b=i
        left=min(a,b)
        right=max(a,b)
        front=right+1
        back=len(nums)-left
        both=(left+1)+(len(nums)-right)
        return min(front,back,both)
        