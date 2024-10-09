class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # first setting 기준
        prefix = list(strs[0])

        for sentence in strs: # flower
            answer = []
            if sentence == strs[0]:
                continue
            alpha = list(sentence) # f l o w
            for num in range(min(len(alpha), len(prefix))): # 4
                if alpha[num] == prefix[num]: # f l o w
                    answer.append(alpha[num])
                else:
                    break
            prefix = answer
            # print("".join(prefix))
        return "".join(prefix)

s = Solution()
strs = [["dog","racecar","car"], ["flower","flow",'flight']]
for a in strs:
    # s.longestCommonPrefix(a)
    print(s.longestCommonPrefix(a))

