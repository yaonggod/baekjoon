while True:
    n = input()
    # 입력이 0일시 수행 종료
    if n == '0':
        break
    # 양쪽 공백과 숫자 개수 - 1개의 중간 공백
    n_length = 2 + len(n) - 1
    # 0은 4, 1은 2, 나머지 숫자는 3을 더함
    for i in range(len(n)):
        if n[i] == '1':
            n_length += 2
        elif n[i] == '0':
            n_length += 4
        else:
            n_length += 3
    print(n_length)