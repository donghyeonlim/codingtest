def solution(s):
    answer = []
    list = s.split(" ")
    for i in list:
        a = ''
        for count in range(len(i)):
            if count % 2 == 0:
                a = a + i[count].upper()
            else:
                a = a +i[count].lower()
        answer.append(a)
    return ' '.join(answer)