def solution(arr):
    arr.remove(min(arr))
    if len(arr) <= 1:
        arr = [-1]
    return arr