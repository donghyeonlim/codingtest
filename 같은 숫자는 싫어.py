def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if not answer[-1] == i:
            answer.append(i)
    return answer