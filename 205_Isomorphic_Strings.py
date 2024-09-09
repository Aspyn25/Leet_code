class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            print(set(s), set(t))
            return False
        s_map = {}  # 이진수로 매핑
        t_map = {}
        s_binary = []  # 이진수 리스트
        t_binary = []
        num = 0

        # 이진수로 매핑
        for char in s:
            if char not in s_map:
                s_map[char] = num
                num += 1
            s_binary.append(s_map[char])

        num = 0

        for char in t:
            if char not in t_map:
                t_map[char] = num
                num += 1
            t_binary.append(t_map[char])

        # 이진수 리스트가 같은지 비교
        if s_binary != t_binary:
            return False

        return True

s= Solution()
print(s.isIsomorphic('bbbaaaba','aaabbbba'))

# 제일 좋은 방법 .index() : 첫번째 등장 인덱스를 알려주는 함수
# class Solution:
#     def isIsomorphic(self, s, t):
#         return [s.index(char) for char in s] == [t.index(char) for char in t]
#
# # 테스트
# s = Solution()
# print(s.isIsomorphic('bbbaaaba', 'aaabbbba'))  # 출력: True