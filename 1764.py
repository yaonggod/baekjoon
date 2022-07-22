n, m = map(int, input().split())
never_heard = []
never_seen = []
for i in range(n):
    never_heard.append(input())
for i in range(m):
    never_seen.append(input())

never_heard_seen = list(set(never_heard) & set(never_seen))
never_heard_seen.sort()
print(len(never_heard_seen))
for i in range(len(never_heard_seen)):
    print(never_heard_seen[i])