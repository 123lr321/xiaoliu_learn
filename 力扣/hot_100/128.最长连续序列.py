def longestConsecutive(nums):
        paw=0
        anw = 0
        begin = 0
        end = 1
        t_nums=list(set(nums))
        t_nums.sort()
        while end < len(t_nums):

            if t_nums[begin] + 1 == t_nums[end]:
                begin = begin + 1
                end = end + 1
            else:
                anw = max(anw, end - paw)
                paw = end
                begin = end
                end = begin + 1
        if paw == 0:
            return len(t_nums)
        return max(anw,end-paw+1)

print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))