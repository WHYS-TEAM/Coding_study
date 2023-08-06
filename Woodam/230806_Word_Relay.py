# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 앞뒤가 맞는지
# 혹은 중복이 있는 지 카운트하고 
# 글자의 인덱스를 호출해서 
# N으로 나눈 뒤 순서 구하기 
import math

def solution(n, words):
    answer = []
    x = [] # 처음 등장한 값인지 판별하는 리스트
    new_word = [] # 중복된 원소만 넣는 리스트
    sol = 0
    sol2 = 0
    
    # 첫번째 검사 : 앞 뒤
    for i in range(len(words)):
        if i > 1 :
            if words[i][0] == words[i-1][-1]:
                pass
            elif words[i][0] != words[i-1][-1] :
                print(i+1)
                sol = i+1
                
    # 2번째 검사 중복 찾기
    for idx, i in enumerate(words):
        if i not in x: # 처음 등장한 원소
            x.append(i)
        else:
            if i not in new_word: # 이미 중복 원소로 판정된 경우는 제외
                new_word.append(i)
                sol2 = idx + 1
    
    if (sol== 0 and sol2 == 0) is True:
        answer = [0,0]
    elif sol > 0 :
        num = sol%n
        order = math.ceil(sol/n)
        answer = [num,order]
    elif sol2 > 0 :
        num = sol2//n
        order = math.ceil(sol2/n)
        answer = [num,order]
    return answer
