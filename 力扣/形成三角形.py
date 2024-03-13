def largestPerimeter(nums):
    nums.sort()
    for i in range(len(nums) - 3, -1 ,-1):
        if nums[i + 2] < nums[i] + nums[i + 1]:
            return nums[i + 2] + nums[i] + nums[i + 1]
    return 0
print(largestPerimeter([1,2,1,2]))