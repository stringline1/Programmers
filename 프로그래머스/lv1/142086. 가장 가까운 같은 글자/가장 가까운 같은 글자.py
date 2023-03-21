def solution(s):
    letters = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in letters.keys():
            letters[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i-letters[s[i]])
            letters[s[i]] = i

    return answer
