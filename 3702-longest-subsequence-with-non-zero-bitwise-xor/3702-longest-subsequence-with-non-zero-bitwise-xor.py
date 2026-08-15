class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        tx=0
        n=len(nums)
        has_nonzero=False
        for i in nums:
            tx^=i
            if i!=0:
                has_nonzero=True
        if not has_nonzero:
            return 0
        if tx!=0:
            return n
        return n-1

        