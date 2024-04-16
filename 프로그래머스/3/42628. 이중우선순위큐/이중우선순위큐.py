def solution(operations):
    answer = []
    for operation in operations:
        oper, num = operation.split(" ")
        try :
            if oper == "I":
                answer.append(int(num))
            elif oper == "D" and num == "1":
                answer.remove(max(answer))
            else :
                answer.remove(min(answer))
        except:
            pass
    if not answer:
        return [0,0]
    answer = sorted(answer, reverse=True)
    answer = [answer[0],answer[-1]]
            
    return answer