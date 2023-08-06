# divmod로 라운드와 플레이어 넘버 계산함

def solution(n, words):
    
    for i in range(1, len(words)):
        w_prev, w_curr = words[i-1:i+1]
        
        if (w_prev[-1] != w_curr[0]) or (w_curr in words[:i]):
            
            return [x+1 for x in divmod(i, n)][::-1]
    
    return [0,0]
