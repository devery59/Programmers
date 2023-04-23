# idea : 광물을 순서대로 캐되 그때마다 도구를 달리할 수 있다! 즉 피로도가 높은 광물이 많은 경우에 다이아를 사용하고 아니면 스톤이나 철 사용
# pain point : 처음에 문제를 제대로 읽지 않아 무조건 순서대로 캐야하도록 코드를 짜서 망했다..
# new knowledge : sorted(list, key=lambda x: (-x[0], -x[1], -x[2])) -> 피로도 높은 광물 순대로 내림차순 가능


def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x

    num_min = sum * 5
    if len(minerals) > num_min:  # 최대 캘 수 있는 광물 수 확인
        minerals = minerals[:num_min]

    # 5개 단위로 나누어 각 종류의 광물이 몇개씩 있는지 확인. 최대 50개이므로 10개의 묶음이 나올 수 있음
    cnt_min = [[0, 0, 0] for x in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt_min[i // 5][0] += 1
        elif minerals[i] == 'iron':
            cnt_min[i // 5][1] += 1
        else:
            cnt_min[i // 5][2] += 1
    # dia > iron > stone 개수 많은 순서대로 묵음을 정렬
    sorted_cnt_min = sorted(cnt_min, key=lambda x: (-x[0], -x[1], -x[2]))

    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p] > 0:
                picks[p] -= 1
                answer += 5 * d + i + s
                break
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                answer += 25 * d + 5 * i + s
                break

    return answer

