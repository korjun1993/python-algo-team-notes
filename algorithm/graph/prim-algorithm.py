import heapq

N = 5  # 정점의 수

# 간선 : {비용, 도착지}
edges = [[] for _ in range(N + 1)]
edges[1] = [(4, 2), (3, 3), (3, 4)]
edges[2] = [(4, 1), (8, 5)]
edges[3] = [(3, 1), (3, 4), (5, 5)]
edges[4] = [(3, 1), (3, 3), (6, 5)]
edges[5] = [(5, 3), (8, 2), (6, 4)]

chk = [False] * (N + 1)  # chk[i] : i번째 정점이 최소 신장 트리에 속해있는가?
cnt = 0  # 현재 선택된 간선의 수
pq = []  # pq[i] = {비용, 출발지, 도착지}

# [1] 임의의 정점을 최소 신장 트리에 포함시킨다.
chk[1] = True
for e in edges[1]:
    heapq.heappush(pq, (e[0], 1, e[1]))

# [2] N - 1 개의 간선을 고를 때 까지 [3-]를 반복한다.
while cnt < N - 1:
    # [3] mst에 포함되지 않은 간선 중 비용이 가장 짧은 간선 선택
    min_edge = heapq.heappop(pq)
    if chk[min_edge[2]]:
        continue
    chk[min_edge[2]] = True
    cnt += 1
    print(min_edge[1], " --> ", min_edge[2], " cost: ", min_edge[0])

    # [4] 새롭게 선택한 정점에서 아직 방문하지 않은 정점으로 향하는 간선을 mst 후보로 선택
    for e in edges[min_edge[2]]:
        if not chk[e[1]]:
            heapq.heappush(pq, (e[0], min_edge[2], e[1]))
