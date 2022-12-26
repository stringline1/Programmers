def solution(n):
    s = n**0.5
    if s == int(s):
        answer = (s+1)**2
    else:
        answer = -1
    return answer