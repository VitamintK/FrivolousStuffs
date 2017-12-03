s=input()
#part 1
prev = s[-1]
ans = 0
for i in s:
    if i == prev:
        ans += int(i)
    prev = i
print(ans)

#part 2
ans = 0
for i in range(len(s)//2):
    if s[i] == s[i+ len(s)//2]:
        ans += 2*int(s[i])
print(ans)
