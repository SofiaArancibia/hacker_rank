# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import median
from math import floor

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

S = list()
for idx, f in enumerate(F):
    l = [X[idx]] * f
    S.extend(l)

X = sorted(S)
n = len(S)

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


print(float(Q3-Q1))


