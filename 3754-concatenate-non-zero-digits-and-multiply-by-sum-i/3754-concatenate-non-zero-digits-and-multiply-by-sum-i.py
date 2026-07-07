class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        x=0
        r=""
        for i in n:
            if i!='0':
                r+=i
        if r=="":
            return 0
        x=int(r)
        s=0
        for i in r:
            s+=int(i)
        return x*s
