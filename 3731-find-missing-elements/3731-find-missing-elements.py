class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        r=[]
        s=set(nums)
        for i in range(a,b+1):
            if i not in s:
                r.append(i)
        return r

        