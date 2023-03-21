def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    total = 0
    for i in range(a-1):
        total += month[i]
    total += b
    
    return day[total%7]