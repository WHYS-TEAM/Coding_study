# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    '''곱해서 total(brown+yellow)가 되는 
    모든 세로(i), 가로(j) 중에
    가장자리를 뺀 격자 수가 yellow와 같은 경우에 [j,i]를 return'''
    
    total = brown + yellow
    
    for i in range(3, int(math.sqrt(total))+1):  # min(i)==3, max(i)==sqrt(total)
        if total % i == 0:
            j = total // i
            if (i-2)*(j-2) == yellow:
                return [j, i]
            
