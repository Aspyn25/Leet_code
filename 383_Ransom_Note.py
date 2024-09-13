# 1 solution
#class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         # hashmap
#         ransom_map = {} # to check ransomNote
#         magazine_map = {} # to check magazine
#
#         for key in ransomNote: # matching the key and index from ransomNote
#             ransom_map[key] = ransom_map.get(key,0) + 1
#         for key in magazine: # matching the key and index from magazine
#             magazine_map[key] = magazine_map.get(key,0) + 1
#
#
#         for key in ransom_map.keys():
#             # if key from ransom is not in magazine too and, value is not from magazine
#             if key not in magazine_map or ransom_map[key] > magazine_map[key] :
#                 return False
#
#         return True

# 2 solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # the rule is ransom can only pick from magazine
        # if not, False
        magazine_list = list(magazine)

        for char in ransomNote: # pick one element from ransom
            if char in magazine_list: # check the one is in magazine
                magazine_list.remove(char)  # 문자가 있으면 사용 후 제거
            else:
                return False  # 없으면 False 반환
        # finishing loop means all element include in magazine
        return True
s = Solution()
print(s.canConstruct('aaa','aaad'))