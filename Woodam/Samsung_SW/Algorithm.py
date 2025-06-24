'''
1. TSP + 비트마스킹
2. Floyd-Warshall
3. Bellman-Ford
4. Dijkstra
5. Lowest Common Ancestor (LCA)
6. Kruskal
7. Topological Sort
8. Segment Tree (Index Tree)
9. Segment Tree + Lazy Propagation
10. Binary Lifting
'''
# 1. TSP + 비트마스킹
# https://konkukcodekat.tistory.com/140
# https://namu.wiki/w/%EC%99%B8%ED%8C%90%EC%9B%90%20%EC%88%9C%ED%9A%8C%20%EB%AC%B8%EC%A0%9C
import sys

INF = 9_876_543  # Java 코드의 9876543 그대로 사용

def main() -> None:
    input = sys.stdin.readline          # I/O 속도 향상
    N = int(input())
    
    # 인접 행렬 입력
    adj = [list(map(int, input().split())) for _ in range(N)]
    
    # d[cur][mask] = cur 도시에 있고 mask 상태(방문 도시 비트셋)일 때 남은 최소 비용
    d = [[0] * (1 << N) for _ in range(N)]

    def tsp(cur: int, mask: int) -> int:
        # 모든 도시를 방문한 경우: 시작점(0)으로 복귀
        if mask == (1 << N) - 1:
            return adj[cur][0]  # 시작점으로 가는 비용(0-0 간선이 0이면 그대로 0)
        
        # 이미 계산된 값이면 재사용
        if d[cur][mask]:
            return d[cur][mask]

        ret = INF
        for nxt in range(N):
            # 아직 방문하지 않은 도시만 선택
            if mask & (1 << nxt):
                continue
            # (cur → nxt) 비용 + nxt 에서 남은 최소 경로
            cost = adj[cur][nxt] + tsp(nxt, mask | (1 << nxt))
            ret = min(ret, cost)

        d[cur][mask] = ret
        return ret

    print(tsp(0, 1))   # 0번 도시에서 출발, 0번 도시만 방문한 상태(mask = 1)

if __name__ == "__main__":
    main()


# Python translations of common graph algorithms and data structures

# 2. Floyd-Warshall
# 모든 지점에서 최단거리 구하기기
# https://velog.io/@kimdukbae/플로이드-워셜-알고리즘-Floyd-Warshall-Algorithm
# https://namu.wiki/w/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
INF = 987654
V, E = map(int, input().split())
adj = [[INF] * (V + 1) for _ in range(V + 1)]
for i in range(1, V + 1):
    adj[i][i] = 0
for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s][e] = c
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if adj[i][k] != INF and adj[k][j] != INF:
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
for i in range(1, V + 1):
    print(*adj[i][1:])

# 3. Bellman-Ford
# 다익스트라 + 음수 간선 
# https://namu.wiki/w/%EB%B2%A8%EB%A8%BC-%ED%8F%AC%EB%93%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://velog.io/@kimdukbae/알고리즘-벨만-포드-알고리즘-Bellman-Ford-Algorithm
INF = 98765
V, E = map(int, input().split())
dist = [INF] * (V + 1)
edges = []
for _ in range(E):
    s, e, c = map(int, input().split())
    edges.append((s, e, c))
dist[1] = 0
for _ in range(V - 1):
    for s, e, c in edges:
        if dist[s] != INF and dist[e] > dist[s] + c:
            dist[e] = dist[s] + c
flag = False
for s, e, c in edges:
    if dist[s] != INF and dist[e] > dist[s] + c:
        flag = True
        break
print(-1 if flag else ' '.join(map(str, dist[1:])))

# 4. Dijkstra
# 한 개의 지점에서 최단거리 구하기기
# https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import heapq
INF = 99999999
V, E = map(int, input().split())
edges = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
for _ in range(E):
    s, e, c = map(int, input().split())
    edges[s].append((e, c))
dist[1] = 0
pq = [(0, 1)]
while pq:
    curW, cur = heapq.heappop(pq)
    for next, nextW in edges[cur]:
        if dist[next] > curW + nextW:
            dist[next] = curW + nextW
            heapq.heappush(pq, (curW + nextW, next))
print(*dist[1:])

# 5. Lowest Common Ancestor (LCA)
# 공통된 조상 구하기. DFS로 Tracking 이후 깊이를 맞추면 된다. 
# https://velog.io/@mjieun/Algorithm-최소-공통-조상Lowest-Common-Ancestor-LCA-Python
# https://stonejjun.tistory.com/63
from collections import deque
N = int(input())
parent = [[0] * (N + 1) for _ in range(10)]
depth = [0] * (N + 1)
edges = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    n = int(input())
    parent[0][i] = n
    edges[n].append(i)
q = deque([1])
while q:
    cur = q.popleft()
    for next in edges[cur]:
        depth[next] = depth[cur] + 1
        q.append(next)
for k in range(1, 10):
    for i in range(1, N + 1):
        parent[k][i] = parent[k - 1][parent[k - 1][i]]
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for k in range(9, -1, -1):
        if depth[b] - depth[a] >= (1 << k):
            b = parent[k][b]
    if a == b:
        return a
    for k in range(9, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return parent[0][a]
print(lca(6, 3))
print(lca(7, 13))

# 6. Binary Lifting
# https://deepdata.tistory.com/965
# https://velog.io/@semoon/Python-LCA%EC%99%80-Binary-Lifting
# LCA에서 2^N 단위로 올라가는걸 뜻함. 시간복잡도가 O(NM) → O(MlogN)으로 변환
d = [[0] * 15 for _ in range(10)]
for i in range(1, 11):
    d[0][i] = i + 1
for k in range(1, 10):
    for i in range(1, 11):
        d[k][i] = d[k - 1][d[k - 1][i]]
N = 5
num = 1
for k in range(9, -1, -1):
    if N >= (1 << k):
        N -= (1 << k)
        num = d[k][num]
print(num)

# 7. Kruskal's Algorithm
# 간선을 오름차순 한 뒤 Greedy 알고리즘 적용. 순환성 있는 경우에만 제거
# https://velog.io/@sy508011/그래프-알고리즘-크루스칼-알고리즘-Kruskal-Algorithm
V, E = map(int, input().split())
p = [i for i in range(V + 1)]
edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        p[y_root] = x_root
cnt, cost = 0, 0
for s, e, c in edges:
    if find(s) != find(e):
        union(s, e)
        cnt += 1
        cost += c
        if cnt == V - 1:
            break
print(cost)

# 8. Topological Sort
# 진입차수 0인것 부터 큐(Queue)에 넣고 다시 Pop하면서 간선 제거. 차례대로 계속 반복
# 이후 큐에서 뺀 순서 대로 정리하면 위상 정렬
# https://velog.io/@kimdukbae/위상-정렬-Topological-Sorting
# https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html
from collections import deque
V, E = map(int, input().split())
edges = [[] for _ in range(V + 1)]
ind = [0] * (V + 1)
for _ in range(E):
    s, e = map(int, input().split())
    edges[s].append(e)
    ind[e] += 1
q = deque(i for i in range(1, V + 1) if ind[i] == 0)
while q:
    cur = q.popleft()
    print(cur)
    for next in edges[cur]:
        ind[next] -= 1
        if ind[next] == 0:
            q.append(next)

# 9. Segment Tree (Index Tree)
arr = [3, 2, 4, 5, 1, 6, 2, 7]
N = len(arr)
tree = [0] * (N * 4)
def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]
def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)
def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)

# 10. Lazy Propagation
lazy = [0] * (N * 4)
def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += lazy[node] * (end - start + 1)
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
def lazy_query(node, start, end, left, right):
    propagate(node, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return lazy_query(node * 2, start, mid, left, right) + lazy_query(node * 2 + 1, mid + 1, end, left, right)
def lazy_update(node, start, end, left, right, diff):
    propagate(node, start, end)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        tree[node] += diff * (end - start + 1)
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return
    mid = (start + end) // 2
    lazy_update(node * 2, start, mid, left, right, diff)
    lazy_update(node * 2 + 1, mid + 1, end, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

