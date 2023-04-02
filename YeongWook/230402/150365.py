#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/150365
##  프로그래머스 코딩테스트 : 미로 탈출 명령어 
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

def solution(n, m, x, y, r, c, k):
    answer = ''
    __FAIL__ = 'impossible'
    
    nVMov = abs(x - r)
    nHMov = abs(y - c)
    nMinDist = nVMov + nHMov
    zRoute = ""
    
    if nMinDist > k or nMinDist % 2 != k % 2:
        return __FAIL__

    ## 추가이동 왕복 횟수를 구함
    nCnt = (k - nMinDist) // 2
    
    ## 추가로 이동해야하는 왕복 이동경로 추가
    a = 0
    for i in range(0, nCnt):
        if x+a == n or r == n:
            zRoute = zRoute + 'lr'
        else:
            zRoute = zRoute + 'du'
            a = a + 1
    
    ## 최소로 이동해야하는 이동경로 추가
    for i in range(0, nVMov):
        if x-r > 0:
            zRoute = zRoute + 'u'
        else:
            zRoute = zRoute + 'd'
    
    for i in range(0, nHMov):
        if y-c > 0:
            zRoute = zRoute + 'l'
        else:
            zRoute = zRoute + 'r'
    
    ## 사전순으로 정렬
    lstRoute = sorted(zRoute)
    
    dx = x
    dy = y
    
    p = 0
    q = 1
    
    ## 실제로 이동해보면서 순서를 맞춤
    while p < k-1:
        if   lstRoute[p] == 'd' and dx < n:
            dx += 1
            p  += 1
            q   = 1
        elif lstRoute[p] == 'l' and dy > 1:
            dy -= 1
            p  += 1
            q   = 1
        elif lstRoute[p] == 'r' and dy < m:
            dy += 1
            p  += 1
            q   = 1
        elif lstRoute[p] == 'u' and dx > 1:
            dx -= 1
            p  += 1
            q   = 1
        else:
            lstRoute[p], lstRoute[p+q] = lstRoute[p+q], lstRoute[p]
            q += 1
    
    answer = ''.join(lstRoute)
    
    return answer