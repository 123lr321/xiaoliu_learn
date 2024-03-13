def threeSum(nums):
        nums.sort()
        list_anw = []
        for i in range(0, len(nums)):
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            beg = i + 1
            end = len(nums) - 1
            while beg < end:
                if beg > i + 1:
                    while (beg < end and nums[beg] == nums[beg - 1]):
                        beg += 1
                if end < len(nums) - 1:
                    while (beg < end and nums[end] == nums[end + 1]):
                        end -= 1
                if nums[i] + nums[beg] + nums[end] == 0 and end > beg:
                    list_anw.append([nums[i], nums[beg], nums[end]])
                    beg += 1
                    end -= 1
                    continue
                if nums[i] + nums[beg] + nums[end] > 0:
                    end -= 1
                if nums[i] + nums[beg] + nums[end] < 0:
                    beg += 1
        return list_anw


print(threeSum([-2, 0, 0, 2, 2]))
