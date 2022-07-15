from math import log10
a = input()
b = input()
c = input()

color = {'black' : 1,
         "brown" : 10,
         "red" : 100,
         "orange" : 1000,
         "yellow" : 10000,
         "green" : 100000,
         "blue" : 1000000,
         "violet" : 10000000,
         "grey" : 100000000,
         "white" : 1000000000}

r = (int(log10(color[a])) * 10 + int(log10(color[b]))) * color[c]
print(r)
