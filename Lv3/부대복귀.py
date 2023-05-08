# idea : 목표지점에 대한 초기값을 -1로 설정하고 목표지점에서 출발하여 각 노드로까지의 거리를 계산

from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    dest = [-1 for _ in range(n + 1)]
    dest[destination] = 0
    graphs = defaultdict(list)
    for a, b in roads:
        graphs[a].append(b)
        graphs[b].append(a)
    deq = deque([destination])
    visited = set([destination])
    while deq:
        node = deq.popleft()
        for x in graphs[node]:
            if x not in visited:
                visited.add(x)
                dest[x] = dest[node] + 1
                deq.append(x)

    return list(dest[s] for s in sources)