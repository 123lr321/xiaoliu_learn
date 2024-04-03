def move_zeroes(nums):
    i=0
    while i<len(nums):
        if nums[i]==0 and set(nums[i:])!={0}:
            del nums[i]
            nums.append(0)
        else:
            i=i+1
    return nums


arr = [0,1,0,223,1,3,0]
print(move_zeroes(arr))

for a in arr:
    print(a)