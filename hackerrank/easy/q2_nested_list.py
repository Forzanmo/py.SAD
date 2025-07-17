n = int(input())
students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = []
for s in students:
    scores.append(s[1])

unique_scores = list(set(scores))
unique_scores.sort()
second_lowest = unique_scores[1]

second_lowest_students = []
for s in students:
    if s[1] == second_lowest:
        second_lowest_students.append(s[0])

second_lowest_students.sort()

for name in second_lowest_students:
    print(name)
