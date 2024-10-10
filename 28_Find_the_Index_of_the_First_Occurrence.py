from wsgiref.util import request_uri


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        answer = -1
        for i in range(len(haystack)):
            # for ii in range(len(needle)):
            if needle == haystack[i:i+len(needle)]:
                answer = i
                break

        return answer








a = [("sadbutsad","sad"),("leetcode","leeto")]
s = Solution()

print(s.strStr("sadbutsad","sad"))