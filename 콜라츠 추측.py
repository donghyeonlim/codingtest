def solution(num):
    count = 0
    if num == 1:
        answer = 0
    elif num >= 1:    
        while True:
            if num % 2 == 0:
                num = num/2
                count = count+1
            elif num % 2 == 1:
                num = num * 3 + 1
                count = count + 1
            if num == 1:
                answer = count
                break
            if count == 500:
                answer = -1
                break
    return answer