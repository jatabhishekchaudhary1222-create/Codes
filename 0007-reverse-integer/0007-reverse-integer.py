class Solution:
    def reverse(self, x: int) -> int:
        ld = 0
        rev = 0
        re = False

        if x < 0:
            re = True
            x = abs(x)

        while x > 0:
            ld = x % 10
            rev = rev * 10 + ld
            x = x // 10

        if re:
            rev = -rev

        if -(2**31) <= rev <= (2**31 - 1):
            return rev
        else:
            return 0


        