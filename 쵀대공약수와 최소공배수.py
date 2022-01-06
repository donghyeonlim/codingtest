def solution(n, m):
    answer = []
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m  % i == 0:
            answer.append(i)
            break
    for a in range(max(n,m),n*m+1):
        if a % n == 0 and a  % m == 0:
            answer.append(a)
            break
    return answer