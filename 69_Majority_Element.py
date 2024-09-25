class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in nums:
            count_num = nums.count(x)
            if count_num > len(nums)/2:
                return  x





s = Solution()
print(s.majorityElement([3,2,3]))

# we can do better like nums.sort() and return nums[len(nums//2)]