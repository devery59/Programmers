# idea : 평균 시간이 가장 짧게 되기 위해서는 process time이 가장 작은거부터 처리해야함.
# 기다리는 놈들은 앞의 놈의 process 타임만큼 waiting time이 더해지는데 이 값이 작을수록 좋기 때문에 작은거부터 처리.

import heapq


def solution(jobs):
    answer = 0  # total_process_time
    time_now = 0  # time after process
    count = 0  # number of processed unit
    start = -1  # time before process
    heap = []

    while count < len(jobs):
        for process_in, process in jobs:
            if start < process_in <= time_now:
                heapq.heappush(heap, [process, process_in])
        if len(heap) > 0:
            process, process_in = heapq.heappop(heap)
            start = time_now
            time_now += process
            answer += (time_now - process_in)
            count += 1
        else:
            time_now += 1
    return int(answer / len(jobs))
