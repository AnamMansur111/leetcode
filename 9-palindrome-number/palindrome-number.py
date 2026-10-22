class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if str(x)==str(x)[::-1]:#v convert the int to sting coz v can find the reverse of string easily ..int not suported
            return True
        else:
            return False        
            
            
        