class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        r=[]
        for i in range(a,b+1):
            if i not in nums:
                r.append(i)
        return r

        