def solution(record):
    answer = []
    logs = {}
    record = [i.split(" ") for i in record]
    for i in record:
        if i[0] == "Enter":
            logs[i[1]] = i[2]
        if i[0] == "Change":
            logs[i[1]] = i[2]
    for j in record:
        if j[0] == "Enter":
            answer.append(f"{logs[j[1]]}님이 들어왔습니다.")
        elif j[0] == "Leave":
            answer.append(f"{logs[j[1]]}님이 나갔습니다.")        
    return answer