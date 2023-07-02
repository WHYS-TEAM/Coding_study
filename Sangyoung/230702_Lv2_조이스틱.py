# 그리디 서치 적용해서 우선 맨 앞을 맞추고 모든 좌우 조합 탐색 후 최소 이동 리턴함
# 다이얼 돌리듯이 기본 'AAA'랑 타켓 'JAZ'을 데큐로 로테이트 시키면서 0번 인덱스 끼리 비교해서 같으면 냅두고 다르면 타겟 알파벳으로 바꿔줌

from collections import deque
from itertools import product

def solution(name):    
    results = []
    
    for rs in product((-1,1), repeat=len(name)-1):
        name_deque = deque(name)
        default = deque('A'*len(name))
        
        for c, r in enumerate([0]+list(rs)):
            default.rotate(r)
            name_deque.rotate(r)
            default[0] = name_deque[0]
            
            if name_deque == default:
                results.append(c)
                break
                
    return min(set(results))+sum([min(ord(l)-ord('A'), ord('Z')-ord(l)+1) for l in name])
  
