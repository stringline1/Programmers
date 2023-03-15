def solution(food):
    a, b = [], []
    for i in range(1,len(food)):
        a.append(str(i)*(food[i]//2))
        b.insert(0, str(i)*(food[i]//2))
    answer = a + ['0'] + b
    
    return ''.join(answer)
