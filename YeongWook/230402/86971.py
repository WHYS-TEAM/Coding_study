#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/86971
##  프로그래머스 코딩테스트 : 미로 탈출 명령어 
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

def solution(n, wires):
    '''
    줄을 끊어 나누어진 송전탑 그룹은 E1 = [], E2 = [] 리스트에 넣기
    
    1번 예제를 예로 들어서
    [4,7] 전선을 끊었다면
    
    4와 연결된 송전탑 갯수 검색
    연결된 송전탑 번호 E1에 넣기
    4와 연결된 송전탑에 연결된 송전탑 검색.. loop
    
    7과 연결된 송전탑 갯수 검색
    연결된 송전탑 번호 E2에 넣기
    7와 연결된 송전탑에 연결된 송전탑 검색.. loop
    
    E1과 E2의 length 절대값 차를 구해 그 중 최소값을 return
    '''
    answer = 9999
    i = 0
    nLen = len(wires)
    
    while i < nLen:
        E1 = []
        E2 = []
        
        ## 자른 전선을 빼서 따로 보관
        Cutted = wires.pop(0)
        
        ## 첫번째 트리 그룹의 송전탑 갯수 구하기
        E1.append(Cutted[0])
        p = 0
        
        while p < len(E1):
            for w in wires:
                ## 연결된 송전탑을 E1에 넣되, 중복된 송전탑이면 패스
                if   E1[p] == w[0] and E1.count(w[1]) == 0:
                    E1.append(w[1])
                elif E1[p] == w[1] and E1.count(w[0]) == 0:
                    E1.append(w[0])
            p += 1
        
        ## 두번째 트리 그룹의 송전탑 갯수 구하기
        E2.append(Cutted[1])
        p = 0
        
        while p < len(E2):
            for w in wires:
                ## 연결된 송전탑을 E2에 넣되, 중복된 송전탑이면 패스
                if   E2[p] == w[0] and E2.count(w[1]) == 0:
                    E2.append(w[1])
                elif E2[p] == w[1] and E2.count(w[0]) == 0:
                    E2.append(w[0])
            p += 1
        
        ## 송전탑 갯수 차이를 구하고, 최소값 저장
        result = abs(len(E1) - len(E2))
        answer = min(answer, result)
        
        ## 자른 전선 복구
        wires.append(Cutted)
        
        i += 1
    
    return answer