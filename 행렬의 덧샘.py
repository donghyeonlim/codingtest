def solution(arr1,arr2):
    import numpy as np
    a = np.array(arr1)
    b = np.array(arr2)
    c = a+b
    answer = c.tolist()
    return answer