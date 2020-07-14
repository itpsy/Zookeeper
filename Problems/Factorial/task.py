n = input()
fact = 1
if int(n) >= 1:
    for i in range(1, int(n) + 1):
        fact *= i
print(fact)
