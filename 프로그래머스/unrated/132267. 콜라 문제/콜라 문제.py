def solution(a, b, n):
    total = 0
    while n>=a:
        total += (n//a)*b
        n += (n//a)*b - (n//a)*a
    
    return total


