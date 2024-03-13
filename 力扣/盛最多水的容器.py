def volume(height):
    volume_anw = 0
    begin = 0
    end = len(height) - 1
    while end > begin:
        if (end - begin) * min(height[begin], height[end]) > volume_anw:
            volume_anw = (end - begin) * min(height[begin], height[end])
        begin += 1
        end -= 1

    return volume_anw
print(volume([1,8,6,2,5,4,8,3,7]))
