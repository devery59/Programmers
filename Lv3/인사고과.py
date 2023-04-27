# idea : 완호의 점수를 미리 저장해놓고 정렬하여 비교하면서 등수 +1
# key point : 정렬시 첫번째 인자는 내림차순으로, 두번째 인자는 올림차순으로 정렬. 
# threshold값을 최신화 해가면서 이미 근태 점수로는 정령되어 있으니 
# 먼저 나온 사람의 동료평가 점수보다 낮은 사람은 인사고과를 받지 못하기 때문에 threshold 높은 사람만 고과 가능해짐.

def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    threshold = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer