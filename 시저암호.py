def solution(s, n):
    answer = ''
    for i in s:
        a = ord(i)
        if a == ord(' '):
            answer = answer + i
        elif a + n > ord('Z') and i.isupper():
            a = a + n - 26
            answer = answer +chr(a)
        elif a +n >ord('z'):
            a = a + n - 26
            answer = answer +chr(a)
        else:
            answer = answer +chr(a+n)
    return answer