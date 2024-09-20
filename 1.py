from collections import Counter
s = input()
map = Counter(s)
for key in map.keys():
    if map[key] > 1:
        print(key, end= " ")
