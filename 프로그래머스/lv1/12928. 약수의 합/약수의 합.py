def solution(n):
    answer = 0
    m = n
    while m > 0:
        if n%m == 0:
            answer += m
        m -= 1
    return answer
