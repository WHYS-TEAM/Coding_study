'''
접근 방법
 - 전체 케이스 탐색 문제 -> BFS, DFS
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
#BFS

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    from collections import deque
    answer = 0
    
    #(탐색 문제 기본 설정) queue: 탐색 후보지
    queue = deque([[numbers[0],0],[-1*numbers[0],0]])
    n = len(numbers) #숫자 개수

    while queue:
        temp, idx = queue.popleft() #탐색 포인트 추출
        idx += 1
        
        # 탐색을 이어 나갈지 결정하는 조건문
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        
        else:
            # target과 일치하는지 확인 하는 부분
            if temp == target:
                answer += 1
    return answer


# DFS

number = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    def dfs(nums, i, n, t):
        ret = 0
        if i==len(nums):
            # target과 일치하는지 확인 하는 부분
            if n==t: 
                return 1
            else: 
                return 0
        ret += dfs(nums, i+1, n+nums[i], t)
        ret += dfs(nums, i+1, n-nums[i], t)
        return ret
    answer = dfs(numbers, 0, 0, target)
    return answer