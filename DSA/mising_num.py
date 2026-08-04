class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        n=len(nums)
        for num in nums:
            sum+=num
        totalsum=(n*(n+1))/2
        return totalsum-sum    

        