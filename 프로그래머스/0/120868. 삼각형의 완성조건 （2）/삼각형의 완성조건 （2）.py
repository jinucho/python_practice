def solution(sides):
    answer = 0
    c = max(sides)
    a = min(sides)    
    answer += len([b for b in range(1,a+c+1) if c - a < b <= c])
    answer += len([b for b in range(1,a+c+1) if c < b < a+c])     
    return answer