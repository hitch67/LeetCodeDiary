class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Symbol	I	V	X	L	C	D	M
        #Value	1	5	10	50	100	500	1,000
        #M = ["","M","MM","MMM"]
        #C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        #X = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        #I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        d = {'M':1000,'D':500,'C':100,'L':50,'X':10, 'V':5, 'I':1}
        num = 0
        for i in range(len(s)):
            num += d[s[i]]
            if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
                num -= d[s[i]]*2
        return num
            
