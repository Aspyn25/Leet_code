class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        items = []
        serval = [nums[0]]

        if not nums:
            return []

        for num in range(1,len(nums)):
            if nums[num] == nums[num-1] + 1:
                serval.append(nums[num])
            else:
                if len(serval) > 1:
                    items.append('{}->{}'.format(serval[0],serval[-1]))
                else:
                    items.append(str(serval[0]))

        if len(serval) > 1:
            items.append('{}->{}'.format(serval[0], serval[-1]))
        else:
            items.append(str(serval[0]))
        return items





s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))