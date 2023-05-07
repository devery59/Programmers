# idea : heap 자료구조에 적들의 값을 저장해놓고 더이상 막지 못하는 상황이 되면 Heap에서 가장 큰 수를 제거

from heapq import heappop, heappush


def solution(n, k, enemy):
    answer, sum_enemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, -e)
        sum_enemy += e
        if sum_enemy > n:
            if k == 0:
                break
            sum_enemy += heappop(heap)
            k -= 1
        answer += 1
    return answer
