def solution(n):
    # 소수를 체크할 리스트 초기화 (모두 True로 설정)
    prime = [True for _ in range(n+1)]

    # 0과 1은 소수가 아님
    prime[0] = prime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:  # i가 소수인 경우
            # i의 배수들을 False로 설정
            for j in range(i+i, n+1, i):
                prime[j] = False

    # 소수가 아닌 수(합성수)의 개수 반환
    return len([x for x in prime[2:] if not x])
