def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        e = bin(arr1[i] | arr2[i])[2:]
        if len(e)<n:
            e = "0" *(n - len(e)) + e
        answer.append(e)
    for i in range(len(answer)):
        answer[i] = answer[i].replace('0', ' ')
        answer[i] = answer[i].replace('1', '#')
    return answer