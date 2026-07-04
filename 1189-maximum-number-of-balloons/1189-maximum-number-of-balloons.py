class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        d={}
        for i in text:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        b=d.get('b',0)
        a=d.get('a',0)
        l=d.get('l',0)//2
        o=d.get('o',0)//2
        n=d.get('n',0)
        return min(b,a,l,o,n)
        