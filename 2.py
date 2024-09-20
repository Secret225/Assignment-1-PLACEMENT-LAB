from collections import Counter
import sys
s = input()
map = Counter(s)
for key in map.keys():
    if map[key] > 1:
        print(False)
        sys.exit()

print(True)
