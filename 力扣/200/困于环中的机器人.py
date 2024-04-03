def is_robot_bounded(instructions):
    instruction=instructions*4
    location = [0, 0]
    k = 0
    for i in instruction:
        if i == 'G':
            if k%4 == 0:
               location[1] += 1
            elif k%4 == 1:
                location[0] += 1
            elif k%4 == 2:
                location[1] -= 1
            else:
                location[0] -= 1
        elif i == 'L':
            k += 1
        elif i == 'R':
            k -= 1
    if __name__ == '__main__':
        print('这是本机')
    else:
        print('这不是')
    if location[0] == location[1] == 0:
        return True
    else:
        return False
