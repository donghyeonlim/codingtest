def solution(price, money, count):
    sum = 0
    a = price
    for i in range(count):
        sum = sum + a
        a = a +price
    answer = sum - money
    if answer < 0:
        answer = 0
    return answer