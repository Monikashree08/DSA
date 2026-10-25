n = int(input())
words = input().split()

vowels = "aeiouAEIOU"
maximum = 0

for word in words:
    count = 0

    for ch in word:
        if ch not in vowels:
            count += 1

    fact = 1
    for i in range(1, count + 1):
        fact *= i

    if count > 1 and fact > maximum:
        maximum = fact

print(maximum)
