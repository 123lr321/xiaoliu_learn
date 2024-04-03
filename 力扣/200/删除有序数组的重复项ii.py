def remove_dup(nums):
    i = 0
    while i < len(nums)-1:
        try:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                while True:
                     if nums[i + 2] == nums[i]:
                         del nums[i + 2]
                     else:
                        break
                i += 2
            elif nums[i] == nums[i + 1]:
                i += 2
            else:
                i += 1
        except:
            break
    return len(nums)
print(remove_dup([1,1,1,2,2,3,3,3,3]))