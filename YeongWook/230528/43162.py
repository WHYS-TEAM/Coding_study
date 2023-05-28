#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/43162
##  프로그래머스 코딩테스트 : 네트워크
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

'''
1. 방문흔적 리스트와 네트워크 갯수 변수 생성
2. 컴퓨터의 갯수만큼 반복
3. 방문흔적이 없을 경우, 연결된 컴퓨터 중 방문할 컴퓨터를 선택 -> 재귀
4. 방문흔적이 있을 경우, 별도 처리 없이 다음 컴퓨터로 넘어감
5. 반복이 종료되면 네트워크 갯수 반환
'''
lstTrace = list()

def solution(n, computers):
    global lstTrace
    
    nCntNet = 0
    
    ## 방문흔적 초기화
    for i in range(n):
        lstTrace.append(0)
    
    ## 연결된 컴퓨터 탐색
    for nComNo in range(n):
        if lstTrace[nComNo] == 0:   ## 방문흔적이 없을 경우
            dfs(computers, nComNo)
            nCntNet += 1    ## dfs 1회 수행할 때 마다 네트워크 1개씩 추가
    
    return nCntNet


def dfs(lstComs, nComNo):
    global lstTrace
    
    ## 방문흔적 남기기
    lstTrace[nComNo] = 1
    
    ## 방문한 흔적이 없는, 현재 컴퓨터에 연결된 컴퓨터가 있다면 연결된 컴퓨터 탐색
    for nIdx, nConnectedYn in enumerate(lstComs[nComNo]):
        if nConnectedYn == 1 and lstTrace[nIdx] == 0:
            dfs(lstComs, nIdx)
    
    return
