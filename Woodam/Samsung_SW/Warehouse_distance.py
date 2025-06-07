'''
[문제]
창고간의 거리의 합을 구해야합니다.
N은 인풋 값의 개수며 N 1개당 (x,y,t) 식으로 주어집니다.

x,y는 위치정보 t는 창고의 종류 정보입니다 (0,1)
거리를 구하는 공식은 맨하탄 거리 공식이며 
t가 같을땐 1을 곱하고 t가 다를땐 2를 곱해야합니다. 

(예시 1)
N : 3
P : [(5,5,0), (5,5,0), (-5,-5,1), (-5,-5,0)

이 경우 P[0]과 P[1]과는 거리를 구하지 않고 
P[3]과 P[4]는 거리를 구하지 않는다.

(제약 조건) 
2 < N < 100,000
python은 12초안에 실행되어야하며
O(n^2) 미만이여야 합니다.

힌트 : 누적합, 분할정복
'''

from collections import defaultdict
import sys

# 파이썬 재귀 호출 깊이 제한 해제 (최대 2^25)
# → 분할 정복이 깊어질 수 있으므로 필요
sys.setrecursionlimit(1 << 25)

# 1. 좌표별 그룹화 함수 정의
def group_positions(P):
    # 같은 위치 (x, y)에 대해 각 t값(0,1)의 개수를 저장하는 딕셔너리
    pos_map = defaultdict(lambda: [0, 0])  # key: (x, y) → value: [t=0 개수, t=1 개수]
    
    for x, y, t in P:
        # 위치(x,y)에서 타입(t)에 해당하는 개수를 1 증가
        pos_map[(x, y)][t] += 1

    grouped = []
    for (x, y), (c0, c1) in pos_map.items():
        # 같은 위치에 t=0 데이터가 있다면 추가
        if c0 > 0:
            grouped.append((x, y, 0, c0))  # (x, y, t, count)
        # 같은 위치에 t=1 데이터가 있다면 추가
        if c1 > 0:
            grouped.append((x, y, 1, c1))
    
    return grouped  # 중복 제거 및 t별 개수 압축된 리스트 반환


# 2. axis(x=0, y=1)에 대해 분할 정복 방식으로 거리합 계산
def manhattan_sum(points, axis):
    def helper(pts):
        if len(pts) <= 1:
            return 0  # 쌍이 없으면 거리 합도 없음

        # 배열을 절반으로 분할
        mid = len(pts) // 2
        left = pts[:mid]
        right = pts[mid:]

        # 좌측과 우측 각각 재귀적으로 거리 계산
        result = helper(left) + helper(right)

        # 누적 합 정보 초기화
        sum_c0 = sum_c1 = 0            # t=0, t=1 타입의 총 개수
        sum_x_c0 = sum_x_c1 = 0        # t=0, t=1 타입의 x좌표 * 개수 누적합
        j = 0                          # 왼쪽 그룹의 인덱스 포인터

        # 오른쪽 그룹의 각 점을 기준으로 왼쪽과의 거리 누적합 계산
        for x_r, _, t_r, c_r in right:
            # 왼쪽 그룹을 순회하면서 오른쪽 값보다 작거나 같은 점들의 누적 정보 수집
            while j < len(left):
                x_l, _, t_l, c_l = left[j]
                if x_l <= x_r:
                    # 타입별로 개수 및 x좌표 누적합 업데이트
                    if t_l == 0:
                        sum_c0 += c_l
                        sum_x_c0 += x_l * c_l
                    else:
                        sum_c1 += c_l
                        sum_x_c1 += x_l * c_l
                    j += 1
                else:
                    break

            # 현재 오른쪽 점(t_r) 기준으로 왼쪽 누적 정보와의 거리 기여 계산
            if t_r == 0:
                # 같은 타입(t=0)
                same = c_r * (x_r * sum_c0 - sum_x_c0)
                # 다른 타입(t=1)
                diff = c_r * (x_r * sum_c1 - sum_x_c1)
            else:
                # 같은 타입(t=1)
                same = c_r * (x_r * sum_c1 - sum_x_c1)
                # 다른 타입(t=0)
                diff = c_r * (x_r * sum_c0 - sum_x_c0)

            # 최종 거리 누적합: 같은 타입은 1배, 다른 타입은 2배
            result += same * 1 + diff * 2

        return result  # 좌+우+좌↔우 거리 총합 반환

    # 기준 축(axis)에 따라 정렬한 후 분할 정복 시작
    points.sort(key=lambda x: x[axis])  # axis=0이면 x축, 1이면 y축 기준
    return helper(points)


# 3. 최종 거리합 계산 함수
def warehouse_distance_sum(P):
    # 1단계: 동일 위치 그룹화 및 타입별 개수 압축
    compressed = group_positions(P)

    # 2단계: x축 방향 거리합 계산
    x_sum = manhattan_sum(compressed, axis=0)

    # 3단계: y축 방향 거리합 계산
    y_sum = manhattan_sum(compressed, axis=1)

    # 4단계: x축 + y축 거리합 반환 → 맨해튼 거리의 정의
    return x_sum + y_sum
