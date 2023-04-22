# idea : priority queue 임이 명시되어 있어 heapq를 사용할까 고민했지만 굳이 사용하지 않아도 될 것 같아 단순 list로 구현
# 다만 아쉬운 점은 각 연산마다 max,min값을 찾아야 하는 연산이 들어가기 때문에 시간복잡도 case가 추가되었다면 heapq를 통해 max,min 따로 관리하는것이 맞아보임

def solution(operations):
    answer = []
    double_priority_queue = [] # 이중 우선순위 큐를 단순 리스트로 구현
    for operation in operations:
        action, value = operation.split() # 각 오페레이션 값을 가져와서 command에 따라 처리
        if action == "I":
            double_priority_queue.append(int(value))
        elif action == "D" and value == "1":
            if len(double_priority_queue) != 0:
                double_priority_queue.remove(max(double_priority_queue))
            else:
                continue
        elif action == "D" and value == "-1":
            if len(double_priority_queue) != 0:
                double_priority_queue.remove(min(double_priority_queue))
            else:
                continue

    if len(double_priority_queue) == 0:
        answer = [0, 0]
    else:
        max_value = max(double_priority_queue)
        min_value = min(double_priority_queue)
        answer = [max_value, min_value]

    return answer
