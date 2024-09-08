class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 해쉬맵으로 연결
        index_map = {}

        for index, num in enumerate(nums):
            if num in index_map:
                # 인덱스 차이가 k 이하인 경우 True 반환
                if abs(index - index_map[num]) <= k:
                    return True
            # 현재 인덱스를 업데이트
            index_map[num] = index

        return False  # 끝까지 조건을 만족하지 않으면 False 반환

s = Solution()
s.containsNearbyDuplicate([1,2,3,4,5,1], 1)