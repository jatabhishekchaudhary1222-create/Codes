class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        cs=0
        c=0
        for i in nums:
            cs+=i
            rs=cs-k
            if rs in d:
                c+=d[rs]
            d[cs]=d.get(cs,0)+1
        return c
        
        