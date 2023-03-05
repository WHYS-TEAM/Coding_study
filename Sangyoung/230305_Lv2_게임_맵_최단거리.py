# https://school.programmers.co.kr/learn/courses/30/lessons/1844


def solution(maps):
    '''모든 좌표를 조회하여 해당 좌표 값을 서치 깊이로 업데이트 하고 적팀 좌표값이 1이 아닌 경우 해당 값을 리턴함
    모든 좌표 조회 후에 exit 실패한 경우 -1 리턴함'''
    
    # 시작 위치
    currs = [(0,0)]
    # 조회한 블록 수 == 스텝 수
    depth = 1
    
    while currs:  # 도달한 좌표 리스트가 존재할 때 까지
        
        # 적 팀 도달 성공 시 exit
        if maps[-1][-1] != 1: return maps[-1][-1]  # 적팀 조회해서 해당 좌표 값이 업데이트 된 경우 해당 값(depth)을 리턴함
        
        # 조회 시작하기 때문에 depth +=1
        depth += 1
        # 현재 도달한 좌표 수 만큼만 currs에서 좌표 pop하고 새로 조회된 좌표를 currs에 스택함
        for _ in range(len(currs)):
            c = currs.pop(0)
            
            # 새로 조회될 좌표 후보 (x,y)에 대해
            for x,y in [(c[0]+d[0], c[1]+d[1]) for d in [(1,0), (-1,0), (0,1), (0,-1)]]:
                # 맵 index range를 충족하고 조회되지 않았으면 벽이 아닌 좌표일 때 해당 좌표 조회
                if (0<=x<len(maps)) and (0<=y<len(maps[0])) and (maps[x][y]==1):
                    # 해당 좌표 값을 depth로 업데이트
                    maps[x][y] = depth
                    # 조회한 좌표를 currs에 스택
                    currs.append((x,y))
    
    # currs가 비어있다면 모든 조회 가능한 좌표를 조회하였는데도 적팀 조회 안 된 것임으로 -1 리턴
    return -1
    
