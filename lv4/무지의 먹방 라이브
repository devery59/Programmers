# idea : heapq에 넣어놓고 네트워크가 끊기기 전에 다 먹을 수 있으면 해당 음식을 제거하고 아니라면 남은 것 중 먹게되는 것을 선택

import heapq


def solution(food_times, k):
    answer = -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  
    while heap:
        t = (heap[0][0] - previous) * food_num
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(heap)
            food_num -= 1
        else:
            idx = k % food_num
            heap.sort(key=lambda x: x[1])
            answer = heap[idx][1]
            break

    return answer
