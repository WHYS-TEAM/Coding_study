'''
[2번문제]
창고간의 거리의 합을 구해야한다.  
N은 인풋 값의 개수다.
N 1개당 (x,y,t) 식으로 주어지며 x,y는 위치정보 t는 창고의 종류 정보다 (0,1)
거리를 구하는 공식은 맨하탄 거리 공식이며 
t가 같을땐 1을 곱하고 t가 다를땐 2를 곱해야한다. 

- 예시 
N : 3
P : [(5,5,0), (5,5,0), (-5,-5,1), (-5,-5,0)

이 경우 P[0]과 P[1]과는 거리를 구하지 않고 
P[3]과 P[4]는 거리를 구하지 않는다.

- 제약 조건 
 2 < N < 100000
python은 12초안에 실행되어야하며
O(n^2) 미만이여야 합니다.

힌트 : 누적합, 분할정복
'''


from collections import defaultdict

# 1. 좌표별 그룹화 (동일 좌표 + 타입 분리)
def group_positions(P):
    pos_map = defaultdict(lambda: [0, 0])  # key: (x, y) → [t=0 개수, t=1 개수]
    for x, y, t in P:
        pos_map[(x, y)][t] += 1

    grouped = []
    for (x, y), (c0, c1) in pos_map.items():
        if c0 > 0:
            grouped.append((x, y, 0, c0))  # (x, y, t, count)
        if c1 > 0:
            grouped.append((x, y, 1, c1))
    return grouped

# 2. 분할 정복 기반 거리 누적합 계산
def manhattan_sum(points, axis):
    def helper(pts):
        if len(pts) <= 1:
            return 0

        mid = len(pts) // 2
        left = pts[:mid]
        right = pts[mid:]

        result = helper(left) + helper(right)

        sum_c0 = sum_c1 = 0
        sum_x_c0 = sum_x_c1 = 0
        j = 0

        for x_r, _, t_r, c_r in right:
            while j < len(left):
                x_l, _, t_l, c_l = left[j]
                if x_l <= x_r:
                    if t_l == 0:
                        sum_c0 += c_l
                        sum_x_c0 += x_l * c_l
                    else:
                        sum_c1 += c_l
                        sum_x_c1 += x_l * c_l
                    j += 1
                else:
                    break

            if t_r == 0:
                same = c_r * (x_r * sum_c0 - sum_x_c0)
                diff = c_r * (x_r * sum_c1 - sum_x_c1)
            else:
                same = c_r * (x_r * sum_c1 - sum_x_c1)
                diff = c_r * (x_r * sum_c0 - sum_x_c0)

            result += same * 1 + diff * 2

        return result

    points.sort(key=lambda x: x[axis])
    return helper(points)

# 3. 최종 계산 함수
def warehouse_distance_sum(P):
    compressed = group_positions(P)
    x_sum = manhattan_sum(compressed, axis=0)
    y_sum = manhattan_sum(compressed, axis=1)
    return x_sum + y_sum
