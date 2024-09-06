
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    final_list = []
    if len(nums) == 2:
        final_list = [0, 1]
        return final_list

    else:
        for i in range(0, len(nums) - 1):
            finda = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == finda:
                    final_list = [i, j]
                    return final_list

print(twoSum([2,7,11,15],9))