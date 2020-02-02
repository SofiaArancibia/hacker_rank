# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

sum_ = 0
sum_w = 0
if len(X)==len(W):
    for idx, val in enumerate(X):
        sum_ += X[idx]*W[idx]
        sum_w += W[idx]
    w_mean = round(sum_/sum_w,1)


print(w_mean)


