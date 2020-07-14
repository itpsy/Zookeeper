n = int(input())
r = int(input())
count = 0

while n > r:
    count += 1
    n /= 2
print(count * 12)
