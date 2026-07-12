class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        r=0
        for i in columnTitle:
            r=r*26+(ord(i)-ord('A')+1)
        return r
        