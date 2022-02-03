def solution(nums):
    from itertools import combinations
    a = [sum(i) for i in combinations(nums,3)]
    for i in a[:]:
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                a.remove(i)
                break
    return len(a)