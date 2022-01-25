def solution(numbers):
    a = 0
    answer = []
    for i in numbers:
        for j in numbers[a+1:]:
            answer.append(j+i)
        a = a+1
    answer = sorted(list(set(answer)))
    return answer