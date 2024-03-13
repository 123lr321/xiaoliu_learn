def singleNumber(nums):
        nums.sort()
        i=0
        k=1
        try:
            while True:
                if nums[i] == nums[k]:
                    k+=1
                else:
                    if k-i>=2:
                        i,k=k,k+1
                    else:
                        return nums[i]
        except:
            return nums[k-1]
print(singleNumber([4,1,2,1,2]))