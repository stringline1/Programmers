def solution(n):
    x = 2
    while True:
        if n%x == 1:
            break
        else: x += 1
    return x