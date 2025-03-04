ls = [1, 2, 3, 4, 5]
result = [i**2 for i in ls if i % 2 == 0]

subs = []

s = "".join(map(str, ls))
print(s)
for i in range(len(s)):
    substring = ""
    for j in range(i+1, len(s)+1):
        substring = s[i:j]
        subs.append(substring)

print(subs)
