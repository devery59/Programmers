# idea : 맨 첫자리를 제외한 나머지 자리는 (n-1)! 만큼이므로 해당 값보다 k가 큰지 작은지 판단해가며 반복한다

import math


def solution(n, k):
    answer = [i for i in range(1, n + 1)]
    stack = []
    k -= 1
    while answer:
        share = k // math.factorial(n - 1)
        stack.append(answer[share])
        del answer[share]
        k = k % math.factorial(n - 1)
        n -= 1

    return stack
