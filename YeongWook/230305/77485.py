#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/77485
##  프로그래머스 코딩테스트 : 행렬 테두리 회전하기
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

def solution(rows, cols, queries):
    answer = []
    
    if rows < 2 or rows > 100:
        return answer
    
    if cols < 2 or cols > 100:
        return answer
    
    # 회전 쿼리가 1개일 경우 제일 첫번째 값을 구해서 리턴
    if len(queries) == 1:
        answer.append( ((queries[0][0]-1) * cols + queries[0][1]) )
        return answer
    
    # 숫자 테이블 생성
    square = []
    for i in range(0, rows):
        nStVal = (cols * i) + 1
        square.append(list(range(nStVal, nStVal + cols)))

    # 입력된 쿼리의 갯수만큼 반복
    for qry in queries:
        nStRow = qry[0] - 1
        nStCol = qry[1] - 1
        nEdRow = qry[2] - 1
        nEdCol = qry[3] - 1
        nPrvVal = square[nStRow][nStCol]
        nCurVal = 0
        lstTrace = []
        
        # 생성된 숫자 테이블을 쿼리에 지정된 방향으로 순서대로 변경
        # 자리가 변경된 숫자는 lstTrace에 저장
        
        #1 오른쪽
        for i in range(nStCol+1, nEdCol+1):
            lstTrace.append(square[nStRow][i])
            nCurVal = square[nStRow][i]
            square[nStRow][i] = nPrvVal
            nPrvVal = nCurVal
        
        #2 아래
        for i in range(nStRow+1, nEdRow+1):
            lstTrace.append(square[i][nEdCol])
            nCurVal = square[i][nEdCol]
            square[i][nEdCol] = nPrvVal
            nPrvVal = nCurVal
        
        #3 왼쪽
        for i in range(nEdCol-1, nStCol-1, -1):
            lstTrace.append(square[nEdRow][i])
            nCurVal = square[nEdRow][i]
            square[nEdRow][i] = nPrvVal
            nPrvVal = nCurVal
        
        #4 위
        for i in range(nEdRow-1, nStRow-1, -1):
            lstTrace.append(square[i][nStCol])
            nCurVal = square[i][nStCol]
            square[i][nStCol] = nPrvVal
            nPrvVal = nCurVal
        
        # 자리가 변경된 숫자가 저장된 lstTrace 리스트에서 최소값 구해서 리턴
        answer.append(min(lstTrace))
    
    return answer