#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/1844
##  프로그래머스 코딩테스트 : 게임 맵 최단거리
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

MIN = 10001

def solution(maps):
    answer = 0
    
    global n
    global m
    global MIN
    
    n = len(maps)    - 1
    m = len(maps[0]) - 1
    
    if maps[n-1][m] == 0 and maps[n][m-1] == 0 :
        answer = -1
    else :
        recur(maps, 0, 0, 1)
        if MIN == 10001:
            answer = -1
        else :
            answer = MIN
    
    return answer


def recur(maps, x, y, dist):
    if x == n and y == m:
        global MIN
        if dist < MIN:
            MIN = dist
        return
    
    # 오른쪽 이동
    if y < m and maps[x  ][y+1] == 1:
        maps[x][y+1] = 2
        recur(maps, x  , y+1, dist+1)
        maps[x][y+1] = 1
    
    # 아래 이동
    if x < n and maps[x+1][y  ] == 1:
        maps[x+1][y] = 2
        recur(maps, x+1, y  , dist+1)
        maps[x+1][y] = 1

    # 위 이동
    if x > 0 and maps[x-1][y  ] == 1:
        maps[x-1][y] = 2
        recur(maps, x-1, y  , dist+1)
        maps[x-1][y] = 1

    # 왼쪽 이동
    if y > 0 and maps[x  ][y-1] == 1:
        maps[x][y-1] = 2
        recur(maps, x  , y-1, dist+1)
        maps[x][y-1] = 1
    
    return