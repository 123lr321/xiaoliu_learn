def ismono(nums):
    if nums[-1]-nums[0]>=0:
        a=1
    else:
        a=-1
    for i in range(2,len(nums)):
        if (nums[i]-nums[i-1])*a<0:
            return False
    return True

