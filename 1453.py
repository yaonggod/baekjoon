n = int(input())
lst = list(map(int, input().split()))

computer = [0 for _ in range(100)]

for i in lst:
    computer[i - 1] += 1
 
count = 0   
for i in range(100):
    if computer[i] == 0 or computer[i] == 1:
        continue
    else:
        count += computer[i] - 1

print(count)