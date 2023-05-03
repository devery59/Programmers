# idea : 차들을 정렬해놓고 하나씩 확인하며 카메라를 추가하는 방식.(진출시점 기준)
# 처음 나간 차량의 진출시점에 설치하고 나머지 차량들은 그 이전에 들어왔는지만 체크. 만약 그 이후에 들어온 차가 있다면 해당 차의 진출 시점으로 최신화
# 아쉬움 포인트 : 정렬하는 방식은 잘 생각했으나 더 효과적으로 나머지 차량을 배제하는 방법이 약간 아쉬웠다. 진입 시점을 기준으로 잡는 것이 아니라 진출시점이 더 효과적이다.

def solution(routes):
    last_camera = -30001
    ordered_routes = sorted(routes, key=lambda x: x[1])
    answer = 0
    for route in ordered_routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
    return answer
