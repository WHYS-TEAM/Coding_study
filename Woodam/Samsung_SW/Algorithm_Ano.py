###############################################################################
# 1. 외판원 순회(TSP) + 비트마스킹 DP
###############################################################################
import sys

INF = 9_876_543          # 충분히 큰 값(무한대 역할)

def main() -> None:
    input = sys.stdin.readline          # 파이썬 기본 input() 보다 5~6배 빠른 I/O
    N = int(input())                    # 도시 수

    # ────────────────────────────────────────────────────────────────────────
    # 인접 행렬: adj[i][j] = i → j 로 가는 비용(0이면 갈 수 없음)
    # ────────────────────────────────────────────────────────────────────────
    adj = [list(map(int, input().split())) for _ in range(N)]

    # d[cur][mask] = cur 도시에 있고, mask(방문비트셋) 상태일 때 **남은 최소 비용**
    # 0: 아직 계산 안 됨 / 값이 있으면 메모이제이션
    d = [[0] * (1 << N) for _ in range(N)]

    # ----------------------------------------------------------------------
    # 깊이우선 + 메모이제이션 : O(N^2 * 2^N)
    # cur  : 현재 위치한 도시
    # mask : 이미 방문한 도시를 비트로 표시 (1 == 방문)
    # ----------------------------------------------------------------------
    def tsp(cur: int, mask: int) -> int:
        # (1) 모든 도시 방문 완료 ⇒ 출발지(0)로 복귀
        if mask == (1 << N) - 1:
            return adj[cur][0] if adj[cur][0] else INF

        # (2) 이미 탐색한 상태라면 그대로 반환
        if d[cur][mask]:
            return d[cur][mask]

        ret = INF
        # (3) 아직 방문하지 않은 다음 도시 시도
        for nxt in range(N):
            if mask & (1 << nxt):         # 이미 방문했다면 skip
                continue
            if adj[cur][nxt] == 0:        # 길이 없으면 skip
                continue
            # (cur → nxt) 이동 비용 + nxt 에서 남은 최소 비용 재귀
            cost = adj[cur][nxt] + tsp(nxt, mask | (1 << nxt))
            ret = min(ret, cost)          # 최소비용 갱신

        d[cur][mask] = ret                # 메모
        return ret

    # 0번 도시에서 출발, 0번만 방문한 상태(mask = 1)
    print(tsp(0, 1))

if __name__ == "__main__":
    main()

###############################################################################
# 2. Floyd-Warshall : 모든 정점 쌍 최단거리 O(V³)
###############################################################################
INF = 987_654

V, E = map(int, input().split())         # 정점, 간선 수
adj = [[INF] * (V + 1) for _ in range(V + 1)]

# 자기 자신까지 거리 = 0
for i in range(1, V + 1):
    adj[i][i] = 0

# 간선 입력 (단방향/가중치)
for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s][e] = c                         # 여러 간선 존재 시, 최소값만 남겨도 OK

# ────────────────────────────────────────────────────────────────────────
# 핵심: “경유지 k”를 하나씩 늘려가며 i→j 최소거리 갱신
# ────────────────────────────────────────────────────────────────────────
for k in range(1, V + 1):                # 경유지
    for i in range(1, V + 1):            # 출발지
        if adj[i][k] == INF:             # i→k 경로 없으면 skip
            continue
        for j in range(1, V + 1):        # 도착지
            # i→k→j 대신 더 짧다면 갱신
            if adj[k][j] != INF and adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

# 결과 출력
for i in range(1, V + 1):
    print(*adj[i][1:])


###############################################################################
# 3. Bellman-Ford : 음수 가중치 허용 & 음수 사이클 탐지 O(VE)
###############################################################################
INF = 98_765
V, E = map(int, input().split())

dist  = [INF] * (V + 1)      # 최단 거리 배열
edges = []                   # (u, v, w) 간선 리스트

for _ in range(E):
    s, e, c = map(int, input().split())
    edges.append((s, e, c))

dist[1] = 0                  # 임의의 시작 정점 = 1

# (V-1)번 반복하면서 최소값 갱신
for _ in range(V - 1):
    for s, e, c in edges:
        if dist[s] != INF:
            dist[e] = min(dist[e], dist[s] + w)

# 음수 사이클 체크 
has_cycle = False
for s, e, c in edges:
    if dist[s] != INF and dist[e] > dist[s] + c:
        has_cycle = True
        break

print(-1 if has_cycle else ' '.join(map(str, dist[1:])))


###############################################################################
# 4. Dijkstra : 단일 시작점 최단거리(양수 가중치) O((V+E) log V) - using heap
###############################################################################
import heapq

INF = 99_999_999
V, E = map(int, input().split())

# 인접 리스트 (u → (v, weight))
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
# 1. 거리 배열 초기화 (무한대)    
dist = [INF] * (V + 1)
# 2. 시작점은 거리 0
dist[1] = 0                             

# 우선선순위 
pq = [(0, 1)]                            # (거리, 정점)

while pq:
    cur_d, u = heapq.heappop(pq)
    if cur_d > dist[u]:                  # stale entry
        continue
    # 연결된 모든 간선 확인
    for v, w in graph[u]: # u → v 거리 w
        if dist[v] > cur_d + w:  # 더 짧은 경로 발견 시
            dist[v] = cur_d + w # 거리 갱신
            heapq.heappush(pq, (dist[v], v)) # 새 경로 추가

print(*dist[1:])

###############################################################################
# 5. LCA(최소 공통 조상) – Binary Lifting 예시
###############################################################################
from collections import deque

LOG = 10                     # 2^10 ≥ 최대 N 깊이(예제 한정)
N   = int(input())           # 노드 수 (1 = root 가정)

parent = [[0]*(N+1) for _ in range(LOG)]  # parent[k][v] = v의 2^k번째 조상
depth  = [0]*(N+1)
tree   = [[] for _ in range(N+1)]

# 부모 정보 입력 (루트의 부모는 0)
for v in range(1, N+1):
    par = int(input())
    parent[0][v] = par
    tree[par].append(v)

# ─ DFS(BFS) 로 depth 계산 ─
q = deque([1])
while q:
    u = q.popleft()
    for v in tree[u]:
        depth[v] = depth[u] + 1
        q.append(v)

# ─ parent 테이블 채우기 : DP
for k in range(1, LOG):
    for v in range(1, N+1):
        parent[k][v] = parent[k-1][ parent[k-1][v] ]

def lca(a: int, b: int) -> int:
    # (1) 깊이 맞추기 – b를 위로 끌어올림
    if depth[a] > depth[b]:
        a, b = b, a
    diff = depth[b] - depth[a]
    for k in range(LOG-1, -1, -1):
        if diff & (1 << k):
            b = parent[k][b]

    # (2) 이미 동일 노드면 종료
    if a == b:
        return a

    # (3) 가장 가까운 조상 직전까지 동시에 점프
    for k in range(LOG-1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    # (4) 바로 위(=parent[0])가 LCA
    return parent[0][a]

print(lca(6, 3))
print(lca(7, 13))

###############################################################################
# 6. Binary Lifting 단순 예제 (k번째 조상 찾기)
###############################################################################
# d[k][i] = i의 2^k 번째 조상
d = [[0]*15 for _ in range(10)]
for i in range(1, 11):       # 1~10 노드
    d[0][i] = i + 1          # 바로 위 조상 예시

for k in range(1, 10):
    for i in range(1, 11):
        d[k][i] = d[k-1][ d[k-1][i] ]

# num = 1의 5단계(=5번째) 조상 구하기
N = 5
node = 1
for k in range(9, -1, -1):
    if N & (1 << k):         # 이 비트가 1이면 해당 단계만큼 점프
        node = d[k][node]
print(node)


###############################################################################
# 7. Kruskal : 최소 신장 트리(MST) – 간선 Greedy + Union-Find
###############################################################################
V, E = map(int, input().split())

parent = list(range(V + 1))          # 초기: 각 정점이 자신을 루트로 갖음

def find(x):
    if parent[x] != x:               # 경로 압축(Path Compression)
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        parent[ry] = rx              # 임의로 ry를 rx 밑으로

edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])       # 가중치 오름차순

pick, total = 0, 0
for u, v, w in edges:
    if find(u) != find(v):           # 사이클 안 생기면 선택
        union(u, v)
        total += w
        pick  += 1
        if pick == V-1:              # MST 완성
            break

print(total)

###############################################################################
# 8. 위상 정렬 (Kahn) : 진입차수 0부터 제거 – DAG 정렬
###############################################################################
from collections import deque

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
indeg = [0]*(V + 1)

for _ in range(E):
    u, v = map(int, input().split())  # u → v
    graph[u].append(v)
    indeg[v] += 1

q = deque([i for i in range(1, V+1) if indeg[i] == 0])

while q:
    u = q.popleft()
    print(u)                          # 정렬 결과 출력
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)


###############################################################################
# 9. 세그먼트 트리 : 구간 합 쿼리 & 단일 갱신
###############################################################################
arr = [3, 2, 4, 5, 1, 6, 2, 7]
N   = len(arr)
tree = [0]*(4*N)          # 트리는 4N 크기로 충분

# 초기화 : 재귀적으로 자식 합을 더해 부모 노드 값 생성
def init(node, l, r):
    if l == r:                         # 리프
        tree[node] = arr[l]
        return tree[node]
    mid = (l + r)//2
    tree[node] = init(node*2, l, mid) + init(node*2+1, mid+1, r)
    return tree[node]

# 구간 합 질의 [ql, qr]
def query(node, l, r, ql, qr):
    if qr < l or r < ql:               # 완전히 벗어난 구간
        return 0
    if ql <= l and r <= qr:            # 완전히 포함
        return tree[node]
    mid = (l + r)//2
    return query(node*2, l, mid, ql, qr) + query(node*2+1, mid+1, r, ql, qr)

# 단일 원소 업데이트(idx, diff)
def update(node, l, r, idx, diff):
    if idx < l or r < idx:
        return
    tree[node] += diff
    if l != r:
        mid = (l + r)//2
        update(node*2, l, mid, idx, diff)
        update(node*2+1, mid+1, r, idx, diff)


###############################################################################
# 10. Lazy Propagation : 구간 업데이트 O(log N)
###############################################################################
lazy = [0]*(4*N)          # 지연 값 저장

# 하위 노드로 lazy 전달
def propagate(node, l, r):
    if lazy[node] != 0:
        tree[node] += lazy[node]*(r - l + 1)  # 현재 구간 길이만큼 누적
        if l != r:                            # 리프가 아니면 자식에 전파
            lazy[node*2]     += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0

# 구간 합 질의 (Lazy 적용)
def lazy_query(node, l, r, ql, qr):
    propagate(node, l, r)
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return tree[node]
    mid = (l + r)//2
    return lazy_query(node*2, l, mid, ql, qr) + lazy_query(node*2+1, mid+1, r, ql, qr)

# 구간 증가 업데이트 [ql, qr] += diff
def lazy_update(node, l, r, ql, qr, diff):
    propagate(node, l, r)
    if qr < l or r < ql:
        return
    if ql <= l and r <= qr:
        tree[node] += diff*(r - l + 1)
        if l != r:
            lazy[node*2]     += diff
            lazy[node*2 + 1] += diff
        return
    mid = (l + r)//2
    lazy_update(node*2, l, mid, ql, qr, diff)
    lazy_update(node*2+1, mid+1, r, ql, qr, diff)
    tree[node] = tree[node*2] + tree[node*2+1]
