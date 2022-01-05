def solution(x):
    a = [int(i) for i in str(x)]    
    i = sum(a)
    return x % i == 0