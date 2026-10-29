s = input()
words = s.split()
pair = []
counts = {}

for word in words:
    st = word[0] + word[-1]
    pair.append(st)

for i in pair:
    counts[i] = pair.count(i)

maxcount = max(counts.values())

for i in pair:
    if counts[i] == maxcount:
        print(i)
        break
