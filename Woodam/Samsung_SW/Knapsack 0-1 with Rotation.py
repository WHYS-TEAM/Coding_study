'''
[코딩 문제]
0-1 문제에 상자의 폭w과 높이h라는 경우의 수를 추가한거야.
상자는 돌릴 수 있어서 w,h의 조합으로 공간 W에 딱 맞게 넣어야 해. 그리고 그때 w*h의 최대값을 구하는거야.

만약 어떤 조합이든 딱 맞게 못넣으면 0을 반환해

제한조건은 5<N<100이고 (N: 상자의 개수)
Python으로 3초야

마지막으로 똑같은 크기의 상자는 여러개 있을 수 있어. 예시 : (2,3) , (3,2) , (3,2)
하지만 똑같은 상자를 다시 쓰는 건 안돼

힌트 :  Dynamic programing
'''

## 기본
def max_area(boxes, W):
    n = len(boxes)
    dp = [0] * (W + 1)

    for i in range(n):      
        # 박스 정의
        w1, h1 = boxes[i]
        # 박스 회전도 정의
        rotations = [(w1, h1), (h1, w1)]

        # 각 상자별로 회전한 2가지 경우를 고려하되, 중복 없이 하나만 사용
        new_dp = dp[:]  # 새롭게 갱신된 값 저장 (중복 사용 방지). TEMP 리스트

        for w, h in rotations:
            for width in range(W, w - 1, -1): # 역순으로 한칸씩 진행
                if dp[width - w] + w * h > new_dp[width]: # 기존 대비 면적이 커지면 # 카데인 알고리즘
                    new_dp[width] = dp[width - w] + w * h # Max값 교체
        dp = new_dp

    return dp[W] if dp[W] > 0 else 0
