class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        l=1
        r=1
        for i in range (len(nums)):
            ans.append(l)
            l=l*nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=r
            r=r*nums[i]
        return ans





        