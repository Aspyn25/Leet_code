class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1 # 중복을 거르면 되는 거라 인덱스 1부터 시작
        # 앞에서부터 확인하면서 중복된 자리에 다른 요소 넣기
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))