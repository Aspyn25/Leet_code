
class Solution(object):
    def isSubsequence(self, s, t):
        s_point = 0 # ab
        t_point = 0 # baab
        answer = False
        if len(s) == 0 :
            answer = True
            return answer
        num = len(s)
        while s_point < len(s) and t_point < len(t):
            if s[s_point] == t[t_point]:
                s_point += 1
                answer = True
                num -= 1
            else:
                answer = False
            t_point += 1
        if num != 0 :
            answer = False

        return answer

s = Solution()
print(s.isSubsequence("acb","asdfbgtdc"))