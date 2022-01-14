def solution(s):
    a = list(s)
    answer= sorted(a,reverse = True )
    return ''.join(answer)