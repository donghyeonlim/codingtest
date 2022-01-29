def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        sum = []
        for j in range(1,i+1):
            if i % j == 0:
                sum.append(j)
        if len(sum) % 2 == 0:
            answer = answer + i
        elif len(sum) % 2 ==1:
            answer = answer - i
    return answer