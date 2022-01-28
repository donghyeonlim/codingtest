def solution(n):
    list = ''
    while True:
        list=list + str(n%3)
        n=n//3
        if n == 0:
            break
    answer = int(list,3)
    return answer