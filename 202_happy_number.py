
def isHappy( n):
    """
    :type n: int
    :rtype: bool
    """
    happy_possible = {} # 해피넘버 가능성 있는 애들
    while True:

        start_num = [int(digit) for digit in str(n)] # 숫자를 하나씩 분리
        squar_num = 0 #제곱수
        for num in start_num :
            squar_num += (num ** 2)
        if squar_num == 1 :
            return True

        if squar_num in happy_possible: #얘는 1이 될 수 없음 / 반복되기 때문에
            return False

        happy_possible[squar_num] = False
        n = squar_num # 제곱수를 n으로 만들기

print(isHappy(2))

# gpt 방법
#
# def isHappy( n):
#
#     seen_numbers = set()  # 중복된 숫자 추적을 위한 set
#
#     while n != 1 and n not in seen_numbers: # n이 1이 아나고, seen_numbers에 없는 숫자일 경우에만 루프
#         seen_numbers.add(n)  # 현재 숫자를 set에 추가
#         n = sum(int(digit) ** 2 for digit in str(n))  # 각 자리수를 제곱한 합을 n으로 설정
#
#     return n == 1  # 1이 되면 True 반환, 아니라면 False 반환

#
# # 테스트
# print(isHappy(19))  # True가 출력됩니다.