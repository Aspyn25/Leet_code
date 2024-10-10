class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aa = "" # customize chars
        for ss in s:
            if ss.isalpha() or ss.isdigit():
               aa += aa.join(ss)
        aa = aa.lower()
        # option 1
        # ans = True
        # compare if it is palindrome
        # aa = list(aa)
        # for x in range(len(aa)):
        #     if aa[x] != aa[len(aa)-x-1]:
        #         ans = False
        #         break
        # return ans

        # option 2
        return aa == aa[::-1]

s = Solution()
print(s.isPalindrome("0P"))
