def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i in range(len(answers)):
        if stu1[i%len(stu1)] == answers[i]:
            count[0] +=1
        if stu2[i%len(stu2)] == answers[i]:
            count[1] +=1
        if stu3[i%len(stu3)] == answers[i]:
            count[2] +=1
    answer = []
    win = max(count)
    for i in range(len(count)):
        if win == count[i]:
            answer.append(i+1)
    # print(answer)
    return answer