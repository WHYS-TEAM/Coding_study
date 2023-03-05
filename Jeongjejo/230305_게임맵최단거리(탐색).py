'''
#접근 방법
- 탐색 문제 -> BFS, DFS -> 최단경로를 찾는 문제 임으로 BFS가 적합해 보임
- BFS -> Queue를 이용
- 기본 map과 동일한 row,column을 갖는 visit을 활용해 중복 탐색 방지
https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
def solution(maps):
    answer = 0
    from collections import deque

    # (매트릭스 탐색 문제 기본 설정)방향: 왼, 오른, 아래, 위
    dx = [-1,1,0,0] 
    dy = [0,0,-1,1]

    #(탐색 문제 기본 설정) queue: 탐색 후보지(시작: (0,0))
    queue = deque([(0,0)])

    # visit: 원점 기준 도달 칸수, 미방문 시 0
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    visit[0][0] = 1


    while queue:
        x, y = queue.popleft() #탐색 포인트 추출

        # 네 방향 탐색을 위한 반복문
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]        

            # 맵 범위 규정하는 조건문 
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):

                # maps 상 도달 가능한 곳 인지 확인하는 조건문
                if maps[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] +1
                    queue.append((nx,ny)) #다음 탐색 포인트 삽입
    if visit[-1][-1]!=0:
        answer = visit[-1][-1]
        return answer
    
