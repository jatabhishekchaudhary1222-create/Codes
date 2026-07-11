class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        ans=0
        for r in range(len(s)):
            while s[r] in d:
                del d[s[l]]
                l+=1
            d[s[r]]=1
            ans=max(ans,r-l+1)
        return ans
        