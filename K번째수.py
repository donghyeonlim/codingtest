def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        list = array[a-1:b]
        list.sort()
        answer.append(list[c-1])
    print(answer)
    return answer
