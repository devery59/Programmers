# idea : subcontainer의 특징이 stack 같기 때문에 stack을 이용해서 구현. 메인 컨테이너에서 온 것을 무조건 subconatiner에 올리고 비교해가는 방식.

def solution(order):
    cnt = 0
    sub_container = []
    index = 1
    while index < len(order)+1:
        sub_container.append(index)
        while sub_container and sub_container[-1] == order[cnt]:
            cnt += 1
            sub_container.pop()
        index+=1
    return cnt