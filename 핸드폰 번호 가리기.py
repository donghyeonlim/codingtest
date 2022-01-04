def solution(phone_number):
    a = phone_number[-4:]
    b = '*' * len(phone_number[0:-4])
    print(a)
    print(b)
    answer = b+a
    return answer