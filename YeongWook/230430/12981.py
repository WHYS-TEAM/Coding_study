#############################
##  https://school.programmers.co.kr/learn/courses/30/lessons/12981
##  프로그래머스 코딩테스트 : 영어 끝말잇기 
##  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
#############################

'''
주어진 단어들로 끝말잇기를 진행
중복되는 단어가 나오거나, 끝말잇기가 성립되지 않는 경우
탈락자 순번, 라운드 횟수를 반환하는 문제

1.   딕셔너리에 주어진 단어들을 키로 넣고 값을 0으로 초기화
2.   끝말잇기를 진행하며 cnt를 0부터 시작해 1씩 증가
3.   탈락여부는 중복단어 또는 끝말잇기 성립 불가
4-1. 딕셔너리의 값이 1보다 큰 경우 중복단어
4-2. 이전 단어의 끝문자가 현재 단어의 첫문자와 다를 경우 끝말잇기 성립불가
5.   탈락자가 나올경우 끝말잇기 종료
     탈락자 번호는 cnt % n + 1, 탈락라운드는 (cnt // n) + 1
     리스트로 만들어 반환
6.   끝말잇기가 무사히 끝난다면 [0,0] 반환

'''
def solution(n, words):
    answer = [0,0]
    cnt = 0
    ls = {}
    
    ## 첫번째 단어의 첫글자 저장
    prevWord = words[0][0]
    
    ## 나온 단어 횟수 카운트 딕셔너리 초기화
    for s in words:
        ls[s] = 0
    
    ## 끝말잇기 시작
    for s in words:
        
        ## 단어 사용횟수 증가
        ls[s] += 1
        
        ## 단어 사용횟수가 2번째거나, 이전 사용 단어와 끝말잇기가 성립되지 않는 경우
        ## 끝말잇기 종료 및 탈락처리
        if ls[s] > 1 or prevWord != s[0]:
            rnd = (cnt // n) + 1    ## 몇번째 반복 라운드인지 체크
            man = cnt % n + 1       ## 몇번째 사람인지 체크
            answer = [man,rnd]
            break
        
        ## 이전 단어의 끝글자 저장
        prevWord = s[-1]
        cnt += 1

    return answer