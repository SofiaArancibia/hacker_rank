from statistics import median
from math import floor

n = int(input())
X = sorted(list(map(int, input().split())))

even = True if n % 2 == 0 else False

Q2 = median(X)

middle = int(n)//2

if even:
    lower_half = X[:int(middle)]
    if X[int(middle)] == Q2:
        upper_half = X[int(middle)+1:]
    else:
        upper_half = X[int(middle):]
else:
    lower_half = X[:int(middle)]
    upper_half = X[int(middle)+1:]

Q1 = median(lower_half)
Q3 = median(upper_half)

print(int(Q1))
print(int(Q2))
print(int(Q3))
