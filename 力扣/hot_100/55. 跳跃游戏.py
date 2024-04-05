def canJump(nums):
        zero_list = []
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                zero_list.append(i)
        for zero_local in zero_list:
            jump_num = 0
            for length in range(zero_local, -1, -1):
                if nums[length] <= jump_num:
                    jump_num += 1
                else:
                    break
            if jump_num > zero_local:
                return False
        return True
print(canJump([3,2,2,0,4]))
