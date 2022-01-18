def solution(dartResult):
    num = ''
    sum = []
    answer = 0
    for i in dartResult:
        if i.isnumeric():
            num = num + i
        elif i == "S":
            sum.append(int(num)**1) 
            num = ''
        elif i == 'D':
            sum.append(int(num)**2)
            num = ''
        elif i == 'T':
            sum.append(int(num)**3)
            num = ''
        elif i == '*':
            if len(sum) <= 1:
                sum[-1] = sum[-1] * 2
            else:
                sum[-1] = sum[-1] * 2
                sum[-2] = sum[-2] * 2
        elif i == '#':
            sum[-1] = sum[-1] * -1
    for i in sum:
        answer = answer +i
    return answer