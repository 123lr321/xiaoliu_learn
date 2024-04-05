def maxSubArray(nums):
    pre_seq = [0] + [nums[0]]
    for i in range(1, len(nums)):
        pre_seq.append(max(nums[i] + pre_seq[i], nums[i]))
    return max(pre_seq)
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
