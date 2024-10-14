
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        brackets=[]
        map = {')':'(','}':'{',']':'['}
        ans = True
        for ss in s:
            if ss not in map:
                brackets.append(ss)
            else:
                if not brackets or brackets.pop() != map[ss]:
                    return False

        return len(brackets) == 0

s = Solution()
print(s.isValid("(){}}{"))