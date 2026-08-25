class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=1
        while(True):
            if k*a not in nums:
                return k*a
            a+=1