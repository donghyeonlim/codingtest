def solution(n):
    a = [i for i in range(1,n+1) if n % i == 0]    
    answer = 0
    for i in a:
        answer = answer + i
    return answer