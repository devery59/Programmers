# idea : 반복적으로 탐색해야 하니 dfs로 접근.
# 처음에 문제를 풀었을 때는 효율성에서 0점을 받았다. 핵심은 어떤 룸을 선택할때마다 해당 룸 다음 빈방을 계산하여 저장해놓아 연산을 줄이는 것!
# new knowledge : sys.setrecursionlimit를 통해 재귀 횟수를 설정할 수 있다.

import sys

sys.setrecursionlimit(10000)


def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        find_empty_room(num, rooms)
    return list(rooms.keys())


def find_empty_room(chk, rooms):
    if chk not in rooms.keys():
        rooms[chk] = chk + 1
        return chk
    empty = find_empty_room(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty
