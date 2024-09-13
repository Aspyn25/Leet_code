
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 # index : for elements not to equal val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # trying to put first
                k += 1
        print(nums)
        return k
s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))
