def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()
    completion.append("아무나")
    for i in range(len(completion)):
        if not participant[i] == completion[i]:
            answer = participant[i]
            break
    
    return answer