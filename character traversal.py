s=input()
result = ""
for ch in s:
    pos = s.index(ch) + 1
    result += ch * pos + "-"
print(result[:-1])
