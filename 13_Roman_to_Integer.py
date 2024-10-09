class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # mapping each roman letter
        Rom_letters = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 
                       'C' : 100, 'D' : 500, 'M' : 1000}
        
        # integer 
        value = 0

        s_list = list(s)
        for i in range(len(s_list)):
            letter = s_list[i]
            if i > 0:
                if s_list[i-1] == 'I' and s_list[i] == 'V' :
                    value = value - 2   
                elif s_list[i-1] == 'I' and s_list[i] == 'X' :
                    value = value - 2   
                elif s_list[i-1] == 'X' and s_list[i] == 'L' :
                    value = value - 20
                elif s_list[i-1] == 'X' and s_list[i] == 'C' :
                    value = value - 20
                elif s_list[i-1] == 'C' and s_list[i] == 'D' :
                    value = value - 200 
                elif s_list[i-1] == 'C' and s_list[i] == 'M' :
                    value = value - 200                   
            value += Rom_letters[letter]
        return value
# for four is not IIII. Instead, the number four is written as IV.
# 900 : DCD / 9 : VIV / 4 : IV / 14 : XIV
s = Solution()
print(s.romanToInt("MCDLXXVI"))


# class Solution(object):
#     def romanToInt(self, s):
#        res = 0
#        roman = {
#         "I" : 1,
#         "V" : 5,
#         "X" : 10,
#         "L" : 50,
#         "C" : 100,
#         "D" : 500,
#         "M" : 1000,
#        }
#        for a,b in zip(s,s[1:]):
#           if roman[a] < roman[b]:
#             res -= roman[a]
#           else:
#             res += roman[a]
#        return res + roman[s[-1]]   