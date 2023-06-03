# new knowledge : 처음 접해보는 Trie(트라이)구조를 사용해서 푸는 것이었다.
# 사실상 트리구조랑 비슷하지만 이것을 단어에 적용시켜 각 chracter별로 비교하여 자식 노드의 개수 chracter를 가지게 된다는 점이 특징이다.

import sys

sys.setrecursionlimit(10 ** 6)


def make_trie(root, word):
    cur_node = root  # root를 반환하지 않고 같은 값을 가르키게 하여 최신화.
    for c in word:
        if c not in cur_node[1]:
            cur_node[1][c] = [0, dict()]

        cur_node[0] += 1
        cur_node = cur_node[1][c]  # 현재 노드를 다음 노드로 변경
    cur_node[0] += 1


def search_target(root, word):
    ret = 0
    cur_node = root

    for c in word:
        if cur_node[0] == 1:  # 자식노드가 없는 경우에만 반환
            return ret
        ret += 1
        cur_node = cur_node[1][c]

    return ret


def solution(words):
    answer = 0
    root = [0, dict()]

    for word in words:
        make_trie(root, word)
    for word in words:
        answer += search_target(root, word)

    return answer
