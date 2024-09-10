class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_map = {}
        magazine_map = {}

        for key in ransomNote:
            ransom_map[key] = ransom_map.get(key,0) + 1
        for key in magazine:
            magazine_map[key] = magazine_map.get(key,0) + 1

        for key in ransom_map.keys():
            if key not in magazine_map or ransom_map[key] > magazine_map[key] :
                return False

        return True

s = Solution()
print(s.canConstruct('aa','d'))