#how to use reduce


class Solution(object):
    def common_prefix(self,str1,str2):
        i = 0
        while(i < len(str1) and i < len(str2)):
            if(str1[i] == str2[i]):
                i += 1
            else:
                break
        return str1[:i]
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        else:
            return reduce(self.common_prefix,strs)
