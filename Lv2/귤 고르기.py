# idea : Counter의 most_common()을 활용하여 각 인자별 개수 및 개수에 따른 내림차순 정렬을 한 뒤 k개 이상이 될때까지 포함시킨다.

from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine = Counter(tangerine).most_common()
    sort = 0
    for size, num in tangerine:
        answer += 1
        sort += num
        if k <= sort:
            break
    return answer
