def maxSubArray(nums):
    anw = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            anw = max(anw, sum(nums[i:j+1]))
    return anw






print(maxSubArray([1]))
