C = int(input())
test_case = []
for i in range(C):
    test_case.append(list(map(int, input().split())))
        
n = len(test_case)
avg = []
for i in test_case:
    avg.append(sum(i[1:])/i[0])

students = [0 for _ in range(n)]   
for i in range(n):
    for j in range(1, len(test_case[i])):
        if test_case[i][j] > avg[i]:
            students[i] += 1

percentage = [0 for _ in range(n)]
for i in range(n):
    percentage[i] = (students[i] / test_case[i][0]) * 100

    
for i in percentage:
    print("%.3f"% i + "%")