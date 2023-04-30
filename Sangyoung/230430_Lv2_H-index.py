# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    
    # sort  
    citations.sort()
    
    h_list  = []  # possible h-idx values
    for h in range(len(citations)+1):  # '전체' 논문 수 포함해서 iter. see test case: [1]
        c = len([x for x in citations if x >= h])  # h이상 인용 논문 count
        if c >= h:  # "h번 이상 인용된 논문(c)이 h편 이상"이면
            h_list.append(h)
    
    print(h_list)
    
    return max(h_list)
    
