# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import floor

size = int(input())
numbers = sorted(list(map(int, input().split())))


middle = int(size/2)

even = True if (size % 2 == 0) else False

if even:
    median = round((numbers[middle] + numbers[middle-1])/2.0, 1)
else:
    median = round(middle,1)

dict_ = {}
max_ = 0
val = 0

for n in numbers:
    if n in dict_.keys():
        dict_[n] += 1
    else:
        dict_[n] = 1

sorted_dict_ = sorted(dict_.items(), key = lambda kv: kv[1], reverse=True)
max_rep = sorted_dict_[0][1]

mode = min([v for v in sorted_dict_ if v[1] == max_rep])[0]

mean = round(sum(numbers)/float((len(numbers))),1)


print(mean)
print(median)
print(mode)
