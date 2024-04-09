def solution(n):
    answer = [0,3,11]
    index = int(n/2)
    if n % 2 != 0:
        return 0 #홀수인 경우는 경우의 수가 없음
    if index < 3 :
        return answer[index]
    for i in range(3,index+1):
        answer.append((answer[i-1]*3 + sum(answer[1:i-1])*2 +2)%1000000007)
    
    return answer[index]


'''
n은 짝수(
n=2일때 경우의 수 : 3 => f(2)
n=4일때 경우의 수 : 3*3 + 2 = 11 ==> f(2)*f(2)+2
n=6일때 경우의 수 : 11*3 + 3*2 + 2 = 41 ==> f(4)*3 + f(2)*2 + 2
...
f(n) = f(n-2)*3 + f(n-4)*2 + ... f(2)*2 + 2
'''