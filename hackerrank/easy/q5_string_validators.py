s = input()

alphas = False
digits = False
alnums = False
lowercases = False
uppercases = False

for ch in s:
    if ch.isalpha():
        alphas = True
    if ch.isdigit():
        digits = True
    if ch.isalnum():
        alnums = True
    if ch.islower():
        lowercases = True
    if ch.isupper():
        uppercases = True

print(alnums)
print(alphas)
print(digits)
print(lowercases)
print(uppercases)
