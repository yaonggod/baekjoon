T = int(input())
test_case = []
for i in range(T):
    test_case.append(list(map(str, input().split())))

# 프린트해야 할 것
# test_case[0][1][0]을 int(test_case[0][0])회 출력
# test_case[0][1][1]을 int(test_case[0][0])회 출력
# test_case[0][1][len(test_case[0][1]) - 1]을 int(test_case[0][0])회 출력
# ...
# test_case[n][1][len(test_case[n][1]) - 1)]을 int(test_case[n][0])회 출력

for i in range(len(test_case)):
    for j in range(len(test_case[i][1])):
        print(test_case[i][1][j] * int(test_case[i][0]), end = "")
    print()


        