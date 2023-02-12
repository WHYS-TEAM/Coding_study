def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(temp)
    
    for i in arr :
        if i != temp: # 비교
            temp = i #바꿔치기
            answer.append(i)

    
    '''
    # 효율성 탈락
    answer = []
    temp = []
    
    for i in range(len(arr)):
        if len(arr) >1000000 :
            break
        att = arr.pop(0)
        if (i == 0) == True : # 처음 시행
            answer.append(att)
            temp.append(att)
        if (i > 0) == True : # 두번째 시행
            if (temp[0] == att) == False :
                answer.append(att)
                temp = [] # 비우기
                temp.append(att)
            else : 
                pass
    '''
    return answer
