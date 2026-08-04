def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n= len(nums)
        map={}
        for i in range(0,n):
            remain=target-nums[i]
            if remain in map:
                return [map[remain],i]
            map[nums[i]]=i
            
print(twoSum([1,2,3,4,5],8))            