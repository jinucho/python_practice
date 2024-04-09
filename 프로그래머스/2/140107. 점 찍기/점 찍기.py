def solution(k, d):
    answer = 0
    d2 = d ** 2
    x = 0
    while x <= d:
        y = 0
        y_max = int((d2 - x**2) **(0.5))
        rest = y_max % k
        answer += (y_max - rest) / k + 1
        x += k

    return answer



'''
k = 입력 변수1
d = 입력 변수2 ==> 제한거리(이하))
x**2 + y**2 == d**2
위 원의 방정식 내부에 존재하는 정수 좌표
k = 1 ,d = 3
x = 0 --> y = 0,1,2,3 
k = 2 ,d = 3
x = 0 --> y = 0,2
'''