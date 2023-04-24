# 내 코드
# idea : 본인의 부모를 바라보게 만드는 다단계 구조 dict를 만들어 seller 값에 따라 다단계 구조를 바라보며 minho를 만날거나 1원 이하가 될 때까지 진행
# pain point : 각 실행마다 stopping point를 만나게 했으나 최악의 경우 10,000 * 100,000 의 경우가 발생. 따라서 시간초과가 발생할 수 있었다.
# 극복 포인트 : 각 반복마다 index 연산을 진행하지 않고 애초에 사람마다 index를 정해놓고 관리했다면 극복할 수 있었을 것!

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    hierarchical = {'minho': ""}
    for i in range(len(enroll)):
        if referral[i] != "-":
            hierarchical[enroll[i]] = referral[i]
        else:
            hierarchical[enroll[i]] = 'minho'
    for j in range(len(seller)):
        money = amount[j] * 100
        person = seller[j]
        while True:
            if hierarchical[person] != 'minho' and money // 10 != 0:
                index = enroll.index(person)
                upper_money = int(money * 0.1) if money * 0.1 >= 1 else 0
                answer[index] += (money - upper_money)
                person = hierarchical[person]
                money = upper_money
            else:
                index = enroll.index(person)
                upper_money = int(money * 0.1) if money * 0.1 >= 1 else 0
                answer[index] += (money - upper_money)
                break
    return answer


# 정답 참고용 코드
def find(parents, money, number, answer):
    # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # 총 사람 수(민호 포함 X)
    answer = [0] * (n + 1)  # 민호 포함
    d = {}  # 이름-번호의 key-value를 가지는 딕셔너리
    parents = [i for i in range(n + 1)]  # 각자 자신을 부모로 초기화
    # 이름-번호로 딕셔너리에 저장
    for i in range(n):
        d[enroll[i]] = i + 1
    # 추천인 입력
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # 칫솔 정산
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]
