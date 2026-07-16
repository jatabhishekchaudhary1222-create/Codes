import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix=[]
        ans=0
        mx=nums[0]
        for i in nums:
            mx=max(mx,i)
            prefix.append(gcd(i,mx))
        prefix.sort()
        l=0
        r=len(nums)-1
        while l<r:
            ans+=gcd(prefix[l],prefix[r])
            l+=1
            r-=1
        return ans
        