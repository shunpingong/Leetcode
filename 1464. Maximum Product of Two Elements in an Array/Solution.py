class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        return (max1-1) * (max2-1)