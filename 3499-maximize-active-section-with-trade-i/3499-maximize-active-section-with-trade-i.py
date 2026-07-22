class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones=s.count('1')
        ans=ones
        i=0
        s='1'+s+'1'
        n=len(s)
        while i<n and s[i]=='1':
            i+=1
        l=0
        while i<n  and s[i]=='0':
            l+=1
            i+=1

        while i<n:
            m=0
            while i < n and s[i] == '1':
                m += 1
                i += 1
            if m==0:
                break
            r=0
            while i < n and s[i] == '0':
                r+= 1
                i += 1

            if r== 0:
                break
            ans = max(ans, ones + l+r)
            l=r
        return ans
            

            


        
        
        

        