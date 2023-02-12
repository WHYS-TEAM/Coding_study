# 프로그래머스
# 가장 큰 수 
# 정렬 문제 
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations

# 내 솔루션
def solution(numbers):
    # 순열로 모든 경우의 수 뽑기
    a = list(permutations(numbers,len(numbers))) 
    sort_list = []
    for i in a :
        # map써서 숫자형 리스트 단일 값으로 변경
        b = ''.join(map(str, i))
        sort_list.append(b)
    result = max(sort_list)
    return result

# 장점 : 쉽게 구현
# 단점 : 절반 정도 runtime error
# https://velog.io/@eunseokim/숫자형-리스트를-단일-값으로-병합하기
