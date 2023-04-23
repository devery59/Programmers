# idea : n개의 수의 합이 s가 되게 할 때, 곱이 최대가 되려면 각 원소의 수의 표준편차가 가장 작아야한다.
# 따라서 s 를 n으로 나눈 몫과 나머지의 값을 활용하여 best set을 구성한다.

def solution(n, s):
    if n > s: # 자연수로만 이루어져야 하므로 해당 케이스는 불가능
        answer = [-1]
    else:
        quotient = s // n
        remainder = s % n
        answer = [quotient] * (n - remainder)
        for _ in range(remainder):
            answer.append(quotient + 1)
    return answer
