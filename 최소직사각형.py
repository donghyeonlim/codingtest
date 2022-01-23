def solution(sizes):
    a = []
    b = []
    for i in sizes:
        c = sorted(i)
        a.append(c[0])
        b.append(c[1])
    answer = max(a) * max(b)
    return answer