def solution(citations):
    answer = 0
    a = sorted(citations,reverse=True)
    for i in range(len(a)):
        if a[i] <= i:
            break
        answer += 1
    return answer