class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for i in words:
            outputs = ""
            for j in i:
                k = ord(j) - 97
                outputs += d[k]
            if outputs not in result:
                result.append(outputs)
        return len(result)
    
        
        
