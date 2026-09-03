def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        my_set=set()
        largest=0
        for i in range(0,n):
            my_set.add(nums[i])
        for i in nums:
            if i-1 not in my_set:
                x=i
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                largest=max(largest,count)

        return largest           

print(longestConsecutive([0,1,8,10,12,2,23]))