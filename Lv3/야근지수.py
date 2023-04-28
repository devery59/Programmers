# idea : heapq를 사용하여 가장 큰수를 반환. 원래 heapq는 가장 작은수를 반환하지만 -1을 곱해서 가장 작업도가 많이 남은 작업을 heappop

import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(0, n):
        m = heapq.heappop(works)
        if m >= 0:
            heapq.heappush(works, m)
            break
        m += 1
        heapq.heappush(works, m)

    answer = 0
    while len(works) > 0:
        m = heapq.heappop(works)
        answer += pow(m * -1, 2)
    return answer