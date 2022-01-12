def solution(n):
    n = n+1
    a = [True] * n
    b = int(n ** 0.5)
    for i in range(2,b+1):
        if a[i] == True:
            for j in range(i+i,n,i):
                a[j] = False
    answer = [ i for i in range(2,n) if a[i] == True]
    return len(answer)