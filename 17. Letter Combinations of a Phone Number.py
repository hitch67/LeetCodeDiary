class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'1':'', '2': 'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        outputs = []
        for i in range(len(digits)):
            if i == 0:
                for j in range(len(d[digits[i]])):
                    outputs.append(d[digits[i]][j])
                print outputs
            else:
                outputs *= len(d[digits[i]])
                outputs.sort()
                for j in range(len(outputs)):
                    outputs[j] += d[digits[i]][j%len(d[digits[i]])]
        return outputs
