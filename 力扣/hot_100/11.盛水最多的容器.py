def maxArea(height):
        volume_anw = 0
        begin = 0
        end = len(height)-1
        while begin < end:
            volume_anw = max(volume_anw,min(height[begin],height[end])*(end - begin))
            if height[begin] > height[end]:
                end -= 1
            else:
                begin += 1
        return volume_anw

print(maxArea([1,8,6,2,5,4,8,3,7]))