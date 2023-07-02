import numpy as np
def solution(name):
    distances = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    count = 0
    loc = 0
    print(distances)
    print("Spell distance(Up and Down distance)의 합: ", np.sum(distances))
    while True:
        #Spell 거리 탐색 sum
        count += distances[loc]
        
        # Stop 조건
        # 1개 인자 씩 확인 더하고 더한 값은 0으로 치환, list의 sum이 0이 되면 stop
        distances[loc] = 0
        if sum(distances) == 0:
            break

        #좌우 이동 거리 중 최소 값 측정
        left = 1
        right = 1
        while distances[loc + right] == 0:
            right += 1
        while distances[loc - left] == 0:
            left += 1

        if left >= right:
            loc += right
            count += right
            print(f"{loc} 번 인자의 좌우 이동 distance: ", right)

        else:
            loc -= left
            count += left
            print(f"{loc} 번 인자의 좌우 이동 distance: ", left)
            
    print("최종 distance의 합: ",count)
    return count