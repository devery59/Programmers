# idea : A의 순서를 고정해놓은 상태에서 각 값을 가져와 B값을 정렬하려고 각종 정렬 알고리즘을 사용해보려고 했지만 시간초과 및 예외 케이스로 실패..
# breaking point : A의 순서를 고정해서 제공한다고 해서 반드시 건드리면 안되는 것은 아니다!
# 결국 중요한 포인트는 A의 원소값보다 B의 원소값 몇개가 더 많냐는 문제이므로 둘다 정렬하고 비교해도 문제가 없었던 것이다..

def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    return answer