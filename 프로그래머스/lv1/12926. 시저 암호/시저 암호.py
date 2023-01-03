def solution(s, n):
    letter = 'abcdefghijklmnopqrstuvwxyz'*2
    Letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    answer = ''
    
    for i in s:
        if i in letter:
            answer += letter[letter.index(i)+n]
        elif i in Letter:
            answer += Letter[Letter.index(i)+n]
        else:
            answer += ' '
            
    return answer