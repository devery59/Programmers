# idea : 특정 수열에서 부분수열의 최대값은 특정 위치(Index)까지의 최대값에서 그 이전(index-1)까지의 최소값은 뺀 수치
# pulse 가 1,-1로 시작하는 두가지 경우에 대해서 모두 연산

def solution(sequence):
    answer = 0
    size = len(sequence)
    start_positive = start_negative = 0
    start_positive_min = start_negative_min = 0
    pulse = 1

    for i in range(size):
        start_positive += sequence[i] * pulse
        start_negative += sequence[i] * (-pulse)
        answer = max(answer, start_positive - start_positive_min, start_negative - start_negative_min)
        start_positive_min = min(start_positive_min, start_positive)
        start_negative_min = min(start_negative_min, start_negative)
        pulse *= -1
    return answer
