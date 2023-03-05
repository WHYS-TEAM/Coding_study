# https://school.programmers.co.kr/learn/courses/30/lessons/42626


import heapq  # 힙은 온전히 정렬된 자료구조는 아니지만 0번 idx는 할상 가장 작은 값임


def solution(scoville, K):
	
    answer = 0  # 음식을 섞은 횟수
    heapq.heapify(scoville)  # 음식 리스트를 힙 자료구조로 변환

    while scoville[0] < K and len(scoville)>1:  # 가장 낮은 스코빌이 K보다 낮음 and 음식이 2개 이상 남았을 때
		
		# 가장 안 매운 음식 2개 pop해서 섞기
		# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        new_food = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
		# 섞기 수행했으니까 answer +1
        answer += 1
		# 새 음식을 scoville에 힙푸시
        heapq.heappush(scoville, new_food)
	
	# 섞을 음식이 남지 않음 and 다 섞은 음식 스코빌 값이 타겟보다 작음
    if len(scoville)==1 and scoville[0]<K:
		# 실패 값 리턴
        return -1
	
	# 가장 안 매운 음식의 스코빌 값이 K 이상일 때 섞은 횟수 리턴
    else:
        return answer
	
