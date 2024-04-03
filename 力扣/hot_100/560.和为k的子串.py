def subarraySum(nums, k):
    begin = 0
    end = 1
    sums = 0
    anw = 0
    while end < len(nums):
        while sums < k:
            sums = sum(nums[begin:end])
            if sums < k:
                end += 1
            if sums == k:
                anw += 1
                begin, end = end, end + 1
                sums = 0
            if sums > k:
                while sums > k:
                    begin += 1
                    if sum(nums[begin:end]) == k:
                        anw += 1
                        begin, end = end, end + 1
                        sums = 0


print(subarraySum(nums=[1, 1, 1], k=2))
