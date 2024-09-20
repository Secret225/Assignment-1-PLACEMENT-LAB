s = input()
k = int(input())
a = 0
num = 1
a1 = 0
a2 = 0
freq = [0] * 26
result = []
for i in range(len(s)):
    freq[ord(s[i])-ord('a')] += 1

for i in range(26):
    if freq[i] == k:
        a += 1
    if freq[i] > k and freq[i] != 2*k:
        a1 += 1
        char1 = chr(ord('a') + i)
    if freq[i] == 2*k:
        a2 += 1
        char2 = chr(ord('a') + i)

for i in range(len(s)):
    result.append("1")

map = {}
if a%2 == 0 or a1 > 0 or a2 > 0:
    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == k:
            if s[i] in map:
                result[i] = "2"
            else:
                if num <= (a//2):
                    result[i] = "2"
                    num += 1
                    map[s[i]] = 1

    if a%2 == 1 and a1 > 0:
        num = 0
        flag = 0
        for i in range(len(s)):
            if s[i] == char1 and num <= k:
                result[i] = "2"
                num += 1

    if a % 2 == 1 and a1 == 0:
        num = 1
        flag = 0
        for i in range(len(s)):
            if s[i] == char2 and num <= k:
                result[i] = "2"
                num += 1
            if freq[s[i] - 'a'] == k and flag == 0 and result[i] == "1":
                result[i] = "2"
                flag = 1

    print("".join(result))
else:
    print("NO")
