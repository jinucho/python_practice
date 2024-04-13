import sys
sys.setrecursionlimit(10000)

def solution(a, b, n):
    answer = 0
    if n < a : 
        return answer
    else : 
        answer += (n//a)*b
        n = n - ((n//a)*a) + ((n//a)*b)
        answer += solution(a,b,n)
        return answer
