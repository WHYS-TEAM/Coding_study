#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/42747
##  프로그래머스 코딩테스트 : H-Index
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################
def solution(citations):
    answer = 0

    '''
    주어진 논문 인용 횟수를 오름차순 정렬
    0부터 시작해 논문의 갯수만큼 인용횟수를 반복 (h)
    h >= citation 이고 h <= citation 인 논문의 갯수를 기록해
    h가 기록한 이상갯수보다 낮거나 같고
    h가 기록한 이히갯수보다 높거나 같으면 H-Index 갱신
    '''
    
    ## 오름차순 정렬
    citations.sort()
    hIdx = 0

    ## 인용횟수를 0부터 시작해 최대 논문갯수만큼 반복
    for h in range(0, len(citations)+1):
        ovr = 0
        und = 0
        
        ## 임의의 인용횟수 h와 주어진 인용횟수를 비교해 hIdx를 구함
        for a in citations:
            if a >= h:      ## 임의 인용횟수 h 이상 값 기록
                ovr += 1
            if a <= h:      ## 임의 인용횟수 h 이하 값 기록
                und += 1

        ## 임의 인용횟수 h가 기록한 이상 값보다 낮거나 같고
        ##                 기록한 이하 값보다 크거나 같다면 hIdx 갱신
        if h <= ovr and h >= und:
            hIdx = h
                
    answer = hIdx
    
    return answer
