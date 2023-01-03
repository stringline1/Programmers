def solution(n, arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        
    for i in range(len(arr1)):
        if len(arr1[i]) != n:
            arr1[i] = '0'*(n-(len(arr1[i]))) + arr1[i]
        if len(arr2[i]) != n:
            arr2[i] = '0'*(n-(len(arr2[i]))) + arr2[i]

    
    answer = []
    
    for i,j in zip(arr1,arr2):
        temp = ''
        for k in range(n):
            if i[k] == '0' and j[k] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)

    return answer