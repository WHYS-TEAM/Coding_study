'''
[최대 서브 배열 문제]
예시1처럼 있을때 2개의 구간을 나눕니다. 
2번 구간은 무조건 1번 구간 다음에 있어야합니다.
다음 공식의 최대값을 구하세요.
그리고 최적화를 하세요. 

(예시 1) nums = [-2,1,-3,4,-1,2,1,-5,4]

* 공식 : 2번 구간 - 1번 구간 
* 제약사항 : 2 < N <10,000입니다. (for문을 2개 이하만 사용가능)
* 힌트 : prefix_sum, 카데인 알고리즘
'''


from typing import List
def max_diff_of_two_subarrays(nums: List[int]) -> int:
    n = len(nums)

    # 1. 왼쪽 최소 서브배열 합 저장
    left_min = [0] * n
    min_sum = float('inf')
    current = 0
    for i in range(n):
        current = min(nums[i], current + nums[i])
        min_sum = min(min_sum, current)
        left_min[i] = min_sum

    # 2. 오른쪽 최대 서브배열 합 저장 (역순으로)
    right_max = [0] * n
    max_sum = float('-inf')
    current = 0
    '''
    i를 n-1부터 0까지 1씩 감소시키며 반복
    start = n-1 : 시작값
    stop = -1 : 반복 종료 조건 (종료값은 포함되지 않음, 즉 0까지 포함됨)
    step = -1 : 1씩 감소
    '''
    for i in range(n - 1, -1, -1):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)
        right_max[i] = max_sum

    # 3. 구간 나누기: left [0..i], right [i+1..n-1]
    answer = float('-inf')
    for i in range(n - 1):
        answer = max(answer, right_max[i + 1] - left_min[i])

    return answer


# 테스트
if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_diff_of_two_subarrays(nums))  # 출력: 10

