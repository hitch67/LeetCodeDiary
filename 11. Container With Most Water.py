class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        n = len(height) - 1
        max_area = 0
        while(n>m):
            if height[m] > height[n]:
                max_area = max(max_area,height[n]*(n-m))
                n = n - 1
            else:
                max_area = max(max_area,height[m]*(n-m))
                m = m + 1
        return max_area
