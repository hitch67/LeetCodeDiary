nums = [2, 7, 11, 15]
target = 9

def twoSum(self, nums, target):
    d = {}
    for i,n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m],i]
        else:
            d[n] = i
