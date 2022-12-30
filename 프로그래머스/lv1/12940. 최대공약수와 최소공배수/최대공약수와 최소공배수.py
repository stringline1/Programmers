def solution(n, m):
    x,y = n,m
    answer = []
    
    while(m):
        n,m = m, n%m
    answer.append(n)
        
    answer.append((x*y)//n)     
    
    return answer