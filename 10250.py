# (101, 201, 301, ... h01), (102, 202, 302, ... h02), ... (10w, 20w, ... h0w)
t = int(input())
test_case = []
for i in range(t):
    test_case.append(list(map(int, input().split())))

answer_list = [] 
for i in range(t):
    h = test_case[i][0]
    w = test_case[i][1]
    n = test_case[i][2]
    w_customer = (n - 1) // h + 1
    if n % h == 0:
        h_customer = h
    else:
        h_customer = n % h
    answer_list.append(h_customer * 100 + w_customer)
    
for i in answer_list:
    print(i)