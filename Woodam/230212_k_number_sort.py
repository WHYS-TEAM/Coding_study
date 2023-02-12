# K번째 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for j in commands :
        temp = []
        temp = array[j[0]-1:j[1]] # 0부터 시작하니까 -1
        temp.sort() # 정렬
        answer.append(temp[j[2]-1]) # 0부터 시작하니까 -1
        
    return answer
