class Solution:
    def minimumPushes(self, word: str) -> int:
        total_push=0
        n=list(word)
        d=len(n)
        for i in range(d):
            if i<8:
                total_push+=1
            elif i<16:
                total_push+=2
            elif i<24:
                total_push+=3
            else:
                total_push+=4
        return total_push
            