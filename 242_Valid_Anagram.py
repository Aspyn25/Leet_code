def isAnagram(s,t):
     if len(s) != len(t):
         return False
     li_s = list(s) # ['a','n','a','g','r','a','m']
     li_t = list(t)
     hash_list_s = {}
     hash_list_t = {}
     num = 0
     for value in li_s:
         hash_list_s[value] =hash_list_s.get(value,0)+ 1 #횟수 체크해야하니까 t도 똑같이 해서 마지막에 두개를 비교하기

     for value in li_t:
         hash_list_t[value] = hash_list_t.get(value, 0) + 1

     if hash_list_s == hash_list_t: # 두 해쉬가 똑같으면 anagram
         return True
     else:
         return False



print(isAnagram('ana','nagaram'))

