n, m = map(int, input().split())
top = []

for i in range(1, n, 2):
    s = '.|.' * i
    top.append(s.center(m, '-'))

for t in top:
    print(t)

print('WELCOME'.center(m, '-'))

for t in reversed(top):
    print(t)
