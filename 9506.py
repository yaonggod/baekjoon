while True:
    n = int(input())
    if n == -1:
        break
    yaksu = []
    for i in range(1, n):
        if n % i == 0:
            yaksu.append(i)
    if sum(yaksu) == n:
        print("{}".format(n) + " = ", end = "")
        for i in range(len(yaksu) - 1):
            print("{}".format(yaksu[i]) + " + ", end = "")
        print("{}".format(yaksu[-1]))
    else:
        print("{}".format(n) + " is NOT perfect.")