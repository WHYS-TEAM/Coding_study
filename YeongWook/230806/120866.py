#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/120866
##  프로그래머스 코딩테스트 : 안전지대
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

'''
1. n*n 배열 중 지뢰 및 지뢰인접지역 제외 갯수 반환하는 문제
2. for문으로 n*n배열 팀섹
3. 인접 지역을 검사하는데, 뒷 지역은 이미 검사하고 지나간 후 이므로
   앞지역(오른쪽, 아래, 오른쪽아래)만 검사
4. 검사한 지역에 지뢰가 있다면 인접구역 위험지역으로 설정
5. 안전지대 갯수 카운트
'''

n = 0

def solution(board):
    answer = 0
    global n
    n = len(board)
    
    for x in range(n):
        for y in range(n):
            
            ## 인근 땅검사
            if board[x][y] == 1:
                SetDangerZone(board, x, y)
            if y < n-1 and board[x][y+1] == 1:
                SetDangerZone(board, x, y+1)
            if x < n-1 and board[x+1][y] == 1:
                SetDangerZone(board, x+1, y)
            if x < n-1 and y < n-1 and board[x+1][y+1] == 1:
                SetDangerZone(board, x+1, y+1)

            ## 안전지대라면 카운트 증가
            if board[x][y] == 0:
                answer += 1
    
    return answer

def SetDangerZone(board, x, y):
    ax = [-1, -1, -1,  0, 0,  1, 1, 1]
    ay = [-1,  0,  1, -1, 1, -1, 0, 1]

    ## 인접 지역 위험지역으로 설정
    for i in range(8):
        tx = x+ax[i]
        ty = y+ay[i]
        if (tx >= 0 and tx < n and
            ty >= 0 and ty < n and
            board[tx][ty] == 0    ):
            board[tx][ty] = 2
                