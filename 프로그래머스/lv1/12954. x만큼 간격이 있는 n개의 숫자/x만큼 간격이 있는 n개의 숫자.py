def solution(x, n):
    answer = []
    y = x
    while len(answer) < n:
        answer.append(y)
        y += x
    return answer