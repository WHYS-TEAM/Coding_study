def solution(people, limit):
    
    # 체중 오름차순 정렬
    people.sort()  
    
    # 왼쪽/오른쪽 인덱스 정의
    left, right = 0, len(people) - 1  
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 있으면 left 한 칸 앞으로 이동
        right -= 1  # 무거운 사람은 항상 타기 때문에 right 한 칸 앞으로 이동
        answer += 1  # 구명보트 한 대 추가
        
    return answer