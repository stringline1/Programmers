def solution(absolutes, signs):
    answer = ''
    signs = list(map(lambda x: '+' if x== True else '-', signs))
        
    for i in range(len(absolutes)):
        answer = answer + signs[i] + str(absolutes[i])
    
    return eval(answer)