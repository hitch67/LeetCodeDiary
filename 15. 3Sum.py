class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        outputs = []
        for i in xrange(len(nums) - 2):
            if len(nums) < 3:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                j = i + 1
                k = len(nums) - 1
                print i,j,k
                while(j<k):
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        #outputs.append((1,1,1))
                        while nums[j] == nums[j+1] and j < len(nums) - 2:
                            j += 1
                        while nums[k] == nums[k-1] and k > 2:
                            k -= 1
                        outputs.append((nums[i],nums[j],nums[k]))
                        if(nums[j] - nums[j+1] > nums[k] - nums[k-1]):
                            k -= 1
                        else:
                            j += 1
        #outputs = list(set(outputs))
        return outputs
