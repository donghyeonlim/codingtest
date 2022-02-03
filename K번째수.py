def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a,b,c = commands
        list = array[a-1:b]
        list.sort()
        answer.append(list[c-1])
    return answer