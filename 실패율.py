def solution(N, stages):
    answer = []
    dic = {}
    peolpe = len(stages)
    for i in range(1,N+1):
        b = stages.count(i)
        if b == 0:
            dic[i] = 0
        else:
            dic[i] = b/peolpe
            peolpe = peolpe - b
    dic = sorted(dic.items(), key=lambda x: x[1],reverse=True)
    for i in dic:
        answer.append(i[0])
    return answer