def stray(nums):

    # sorted_num = sorted(arr)

    # if sorted_num[0] != sorted_num[1]:
    #     return sorted_num[0]
    # if sorted_num[-1] != sorted_num[-2]:
    #     return sorted_num[-1]

    # for num in range(1, len(arr)-1):
    #     if sorted_num[num] != sorted_num[num - 1] and sorted_num[num] != sorted_num[num + 1]:
    #         return sorted_num[num]

    # for x in arr:
    #     if arr.count(x) == 1:
    #         return x
    # for num in nums:
    #     if nums.count(num) > 1:
    #         return True
    #     else:
    #         return False
    # counts = {}
    # for num in nums:
    #     counts[num] = counts.get(num, 0) + 1
    #     if counts[num] > 1:
    #         return True
    # return False

    counts = set()
    for num in nums:
        if num not in counts:
            counts.add(num)
        else:
            return True
    return False


print(stray([2, 14, 18, 22, 22]))


def isAnagram(s, t):

    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        return True
    return False


isAnagram("anagram", "nagaram")
