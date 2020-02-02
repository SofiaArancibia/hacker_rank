# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

N = int(input())
X = list(map(int, input().split()))

mean = float(sum(X)/N)

sum_ = 0
for idx, n in enumerate(X):
    sum_ += (X[idx] - mean)**2

std_dev = sqrt(sum_/N)

print(std_dev)
