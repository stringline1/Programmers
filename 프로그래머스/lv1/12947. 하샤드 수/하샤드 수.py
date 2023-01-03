def solution(x):
    num = 0
    y = x
    while y > 0:
        num += y%10
        y //= 10
        
    if x % num == 0:
        return True
    else:
        return False