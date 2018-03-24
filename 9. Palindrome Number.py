#fking meanless problem
#one line :   return str(x)[::-1] == x


#string baned
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        b = x 
        y = 0
        while(b>0):
            y = y * 10 + b % 10
            b = b / 10
        return y==x
        










