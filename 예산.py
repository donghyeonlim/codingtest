def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in d:
        sum = sum + i
        if sum > budget:
            break
        answer = answer + 1  
    return answer