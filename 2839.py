n = int(input())
bag_3 = 0
bag_5 = 0

def bag(n):
    global bag_5
    global bag_3
    if n < 0:
        # print(n)
        return -1
    elif n > 0:
        if n % 5 == 0:
            # print(n)
            bag_5 = n // 5
            n -= 5 * (n // 5)
            # print(n)
            # print("bag_5 = {}".format(bag_5))
        else:
            # print(n)
            bag_3 += 1
            n -= 3
            # print("bag_3 = {}".format(bag_3))
        return bag(n)
    else:
        # print(n)
        return bag_3 + bag_5
            
print(bag(n))
