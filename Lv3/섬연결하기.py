# idea : 크루스칼 알고리즘을 사용하여 연결 리스트를 오름차순으로 정렬하여 사이클 발생 여부를 확인하고 발생하지 않으면 spanning tree 포함. 발생하면 스킵

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


def solution(n, costs):
    answer = 0
    parent = [0] * (n + 1)
    costs = sorted(costs, key=lambda x: x[2])
    for i in range(1, n + 1):
        parent[i] = i
    for edge in costs:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer
