n = int(input())
players_firstletter = []
for i in range(n):
    players_firstletter.append(input()[0])
players_firstletter.sort()    
players_firstletter_set = set(players_firstletter)
letters = []
for i in players_firstletter_set:
    if players_firstletter.count(i) >= 5:
        letters.append(i)
letters.sort()

if len(letters) == 0:
    print("PREDAJA")
else:
    for i in letters:
        print(i, end = "")
