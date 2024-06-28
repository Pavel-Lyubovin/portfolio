# Generate Pascal triangle
# https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA_%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8F

n = int(input())

li = [1]
print(*li)
for i in range(n - 1):
    for j in range(len(li) - 1):
        li[j] = li[j] + li[j + 1]
    li.insert(0, 1)
    print(*li)