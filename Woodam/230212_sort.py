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
# https://velog.io/@eunseokim/숫자형-리스트를-단일-값으로-병합하기\


# 또 다른 풀이 1
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    # Bool - Bool
    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return str(answer)
# ref : https://wikidocs.net/109303


# 또 다른 풀이2
## 비추
## Ref: https://esoongan.tistory.com/103
def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열 숫자 비교 이용
    # 앞자리부터 비교. *3은 제한된 값 1000. 
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


