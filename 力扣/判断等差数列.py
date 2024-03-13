def exam(arr):
    b = len(arr)
    for i in range(0, b):
        for k in range(i, b):
            if arr[i] < arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
    for i in range(2, b):
        if arr[i] - arr[i - 1] != arr[1] - arr[0]:
            return False
    return True
