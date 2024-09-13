class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        t = m + n - 1
        while n > 0 and m > 0 : # if n or m will be 0, stop this loop
            if nums1[m-1] < nums2[n-1]:
                nums1[t] = nums2[n-1] # the bigger one put in the last index
                n -= 1
            else:
                nums1[t] = nums1[m-1]
                m -= 1
            t -= 1
        while n > 0 : # if left n (technically m is nums1 so, we dont need to change it, already in)
            nums1[t] = nums2[n-1]
            n -= 1
            t -= 1
        print(nums1)

s = Solution()
print(s.merge([2,0],1,[1],1))
