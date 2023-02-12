#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/42587
##  프로그래머스 코딩테스트 : 프린터
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

def solution(priorities, location):
    answer = 0
    YES = True
    NO = False
    
    lstPrio = priorities
    nLstLen = len(lstPrio)
    lstIdx = list(range(nLstLen))
    nIdx = 0
    
    ## Loop until Print location Index
    while True:
        ## Init PrintYn
        bPrintYn = YES
        
        ## Check High Prio Doc
        for nDocPrio in lstPrio[nIdx+1:]:
            ## Exist High Prio then Move Prio
            if lstPrio[nIdx] < nDocPrio:
                ## Pop and Append Last
                tmp = lstPrio.pop(nIdx)
                lstPrio.append(tmp)
                tmp = lstIdx.pop(nIdx)
                lstIdx.append(tmp)
                
                ## Init PrintYn
                bPrintYn = NO
                break
        
        ## No High Prio then Print Doc(increase idx)
        if bPrintYn == YES:
            ## Find location Index then Exit Loop
            if lstIdx[nIdx] == location:
                break
            nIdx = nIdx + 1
    
    answer = nIdx + 1
    
    return answer