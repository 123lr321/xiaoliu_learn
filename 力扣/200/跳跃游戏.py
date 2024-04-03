def canJump(nums):
    ling_list = [i for i, x in enumerate(nums) if x == 0]
    if not ling_list:
        return True
    numb = 0
    if ling_list[-1] == len(nums) - 1:
        del ling_list[-1]
    for i in ling_list:
        for j in range(i - 1, -1, -1):
            if nums[j] > i - j:
                numb += 1
                break
    if numb == len(ling_list):
        return True
    else:
        return False


print(canJump([3, 0, 0, 0]))
