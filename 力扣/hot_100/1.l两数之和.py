def twoSum(nums, target):
    for i in range(0,len(nums)):
        b=target-nums[i]
        if b in nums[i+1:]:
            return [i,nums[i+1:].index(b)+i+1]