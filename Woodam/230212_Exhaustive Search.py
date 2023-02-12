# 완전 탐색
# 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
  
    # 큰 값들 모음
    max_list = []
    for x in sizes : 
        max_list.append(max(x))
    
    # 작은 값들 모음
    min_list = []
    for x in sizes : 
        min_list.append(min(x))
    
    # 큰 값중 큰 값 * 작은 값중 큰 값    
    answer = max(max_list) * max(min_list)
    return answer


