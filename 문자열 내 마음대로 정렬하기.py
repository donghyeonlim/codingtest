def solution(strings, n):
    # answer = sorted(strings, key=lambda x : x[n])
    # answer = sorted(sorted(strings, key=lambda x : x[n]))
    answer = sorted(sorted(strings), key=lambda x : x[n])
    return answer