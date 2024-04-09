def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    else:
        answer = [s//n]*n
        if s%n != 0 :
            answer[-(s%n):] = [(s//n)+1]*(s%n)
    return answer