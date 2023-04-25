# idea : 해시 알고리즘은 기본적으로 dict 자료형을 사용하여 구현한다.
# pain point : dict로 구현하려고 하였지만 1,2위라는 순위의 개념을 적용시키기위한 방법을 떠올리지 못했다.
# dict 자료형은 순서가 없다고 배워 dict에서 순위를 부여하여 1,2위를 가려낼 방법을 생각해내지 못했다.
# new knowledge : sorted함수에 dict.items() 값을 인자로 넘겨주어 연산하면 반환 결과가 list로 나오게 된다. 이를 활용하여 dict를 정렬할 수 있다.

def solution(genres, plays):
    answer = []

    dic1 = {}  # 각 장르별 1,2위를 뽑기 위한 dict
    dic2 = {}  # 재생횟수 1,2위인 장르를 뽑기위한 dict

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(index, play)]
        else:
            dic1[genre].append((index, play))

        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play

    for (key, value) in sorted(dic2.items(), key=lambda x: -x[1]):
        for (index, play) in sorted(dic1[key], key=lambda x: -x[1])[:2]:
            answer.append(index)

    return answer
