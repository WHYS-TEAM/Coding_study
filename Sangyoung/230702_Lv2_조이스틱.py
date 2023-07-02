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
  
