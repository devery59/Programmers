# idea : 투포인터 문제로 모든 케이스에 대해 체크하여 가장 긴 값으로 최신화

def solution(s):
    answer = 0
    for start in range(len(s)):
        for end in range(start, len(s) + 1):
            if is_palindrome(s[start:end]):
                answer = max(answer, end - start)
    return answer


def is_palindrome(word):
    return word == word[::-1]
