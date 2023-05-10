# idea : 유저와 밴 리스트의 길이가 각각 8개밖에 되지 않기 때문에 밴 리스트 길이만큼의 가능한 조합의 경우를 모두 구해 비교한다.

from itertools import permutations


def check(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            if j == '*':
                continue
            if i != j:
                return False
        return True


def solution(user_id, banned_id):
    answer = []

    for possible_case in permutations(user_id, len(banned_id)):
        count = 0
        for user, ban in zip(possible_case, banned_id):
            if check(user, ban):
                count += 1

        if count == len(banned_id):
            if set(possible_case) not in answer:
                answer.append(set(possible_case))

    return len(answer)
