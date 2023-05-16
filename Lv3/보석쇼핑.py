# idea : 정답을 gems 리스트의 최대 길이로 잡아놓고 투포인터를 만들어 해당 길이가 gem 종류의 사이즈와 일치할때마다 확인 후 업데이트

def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    start, end = 0, 0
    buy_list = {gems[0]: 1}

    while start < len(gems) and end < len(gems):
        if len(buy_list) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                buy_list[gems[start]] -= 1
                if buy_list[gems[start]] == 0:
                    del buy_list[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems):
                break
            buy_list[gems[end]] = buy_list.get(gems[end], 0) + 1

    return [answer[0] + 1, answer[1] + 1]