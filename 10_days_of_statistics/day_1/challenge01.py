# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import floor

n = int(input())
X = list(map(int, input().split()))

def median(X, n):
    middle = int(n/2)
    even = True if (n % 2 == 0) else False
    if even:
        median = round((X[middle] + X[middle-1])/2.0, 1)
        idx = -1
    else:
        median = X[int(floor(middle))]
        idx = int(floor(middle))
    return median, idx

def remove_median(X,median):

    return [elem for elem in X if elem != median]

X=sorted(X)


Q2, idx = median(X, n)


#X = remove_median(X, Q2)


if idx != -1:
    lower_half = X[:idx]
    upper_half = X[idx+1:]
else:
    lower_half = X[:len(X)/2]
    upper_half = X[(len(X)/2):]



Q1, _ = median(lower_half, len(lower_half))
Q3, _ = median(upper_half, len(upper_half))

print(int(Q1))
print(int(Q2))
print(int(Q3))



# Failing in hackerrank website due to IndexError. Tested in other environments and it works fine
