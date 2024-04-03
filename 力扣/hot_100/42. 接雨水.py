def trap(height):
            anw = 0
            height_n = len(height)
            left_max = [height[0]] + [0] * (height_n-1)
            for i in range(1, height_n):
                left_max[i] = max(height[i], left_max[i - 1])
            right_max = [0] * (height_n-1) + [height[height_n-1]]
            for i in range(height_n-2,-1,-1):
                right_max[i] = max(height[i], right_max[i + 1])
            for i in range(0, height_n):
                anw += min(left_max[i], right_max[i]) - height[i]
            return anw


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
