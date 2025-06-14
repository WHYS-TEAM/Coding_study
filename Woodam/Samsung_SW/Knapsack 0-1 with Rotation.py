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

## 함수
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

# 테스트 케이스
def test_max_area(func):
    test_cases = [
        ([(2, 3), (3, 2), (3, 2)], 5, 12), # 회전하면 셋다 같음
        ([(1, 2), (2, 1), (3, 1)], 7, 0), # 맞는게 없을때
        ([(2, 2), (2, 2), (2, 2)], 4, 8), # 셋이서 같음
        ([(5, 3), (4, 2)], 7, 23), # 회전해서 맞음
        ([(i % 10 + 1, (i * 2) % 10 + 1) for i in range(1, 101)], 100, -1),  # 성능 확인용
    ]

    for i, (boxes, W, expected) in enumerate(test_cases, 1):
        result = func(boxes, W)
        status = 'PASS' if result == expected or expected == -1 else 'FAIL'
        print(f"Test Case {i}: {status} (Output: {result})")


'''
# 정렬 버전
def max_area_sorted(boxes, W):
    n = len(boxes)
    dp = [0] * (W + 1)

    # 상자 회전 포함 후 넓이 기준 정렬
    all_boxes = []
    for w, h in boxes:
        all_boxes.append((w, h))
        all_boxes.append((h, w))
    all_boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

    # 상자 1개당 2개 회전쌍이 생기므로 2개씩 묶어서 한 번만 사용
    for i in range(0, len(all_boxes), 2):
        w1, h1 = all_boxes[i]
        w2, h2 = all_boxes[i + 1]
        new_dp = dp[:]

        for w, h in [(w1, h1), (w2, h2)]:
            for width in range(W, w - 1, -1):
                if dp[width - w] + w * h > new_dp[width]:
                    new_dp[width] = dp[width - w] + w * h
        dp = new_dp

    return dp[W] if dp[W] > 0 else 0
'''
'''
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int max_area(const vector<pair<int, int>>& boxes, int W) {
    int n = boxes.size();
    vector<int> dp(W + 1, 0);

    for (int i = 0; i < n; ++i) {
        int w1 = boxes[i].first;
        int h1 = boxes[i].second;

        vector<pair<int, int>> rotations = {{w1, h1}, {h1, w1}};
        vector<int> new_dp = dp;  // 복사: 상자 1개당 1회만 사용하기 위함

        for (const auto& rot : rotations) {
            int w = rot.first;
            int h = rot.second;

            for (int width = W; width >= w; --width) {
                if (dp[width - w] + w * h > new_dp[width]) {
                    new_dp[width] = dp[width - w] + w * h;
                }
            }
        }

        dp = new_dp;
    }

    return dp[W] > 0 ? dp[W] : 0;
}
'''