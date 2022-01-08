def solution(n):
    a = [int(i) for i in str(n)]
    a.sort(reverse=True)
    b = [str(i) for i in a]
    answer = int(''.join(b))
    return answer