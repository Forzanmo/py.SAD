n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    scores = data[1:]
    
    total = 0.0
    count = 0
    for score in scores:
        total += float(score)
        count += 1

    students[name] = total / count

query = input()
print(format(students[query], '.2f'))
