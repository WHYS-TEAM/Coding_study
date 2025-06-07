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

