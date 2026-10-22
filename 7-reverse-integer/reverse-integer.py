class Solution:
    def reverse(self, x: int) -> int:
        k=str(abs(x))[::-1]
        k=int (k)
        if x<0:
            k= -k
        if k<-(2**31) or k>2**31-1:
            return 0
        return k        
        