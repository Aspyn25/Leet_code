
def wordPattern( pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    pattern_li = list(pattern) # 리스트로 정렬
    s_list = s.split()  # 리스트로 정렬

    # 길이가 다르면 어차피 다른 거라 바로 거르기
    if len(pattern_li) != len(s_list):
        return False

    # 패턴 별 매칭하기
    zip_li = list(zip(pattern_li,s_list))

    # 중복 찾기
    has_map = {}
    value_map ={}

    for key, value in zip_li:
        # 패턴에 키 값 없으면 매칭
        if key not in has_map:
            has_map[key] = value
        # 이미 매칭된 키가 있는데 바꾸면 anagram이 아님
        elif has_map[key] != value:
            return False
        # 또한 s에도 중복이 있는지 체크해야함
        if value not in value_map:
            value_map[value] = key
        elif value_map[value] != key:
            return False

    return True


print(wordPattern('abba','dog dog dog dog'))