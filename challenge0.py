
from math import floor

size = int(input())
numbers = sorted(list(map(int, input().split())))


middle = int(size/2)

even = True if (size % 2 == 0) else False

if even:
    median = (numbers[middle] + numbers[middle-1])/2
else:
    median = int(floor(middle))

dict_ = {numbers[0]:1}
max_ = 0
val = 0
count = 0
for n in numbers[1:]:
    if n in dict_.keys():
        dict_[n] += 1
    else:
        dict_[n] = 1
    count += 1
    
if sum(dict_.values()) == size:
    mode = min(dict_.keys())
else:
    for n in dict_.keys():
        if dict_[n]>max_:
            max_ = dict_[n]
            mode = n

mean = sum(numbers)/(len(numbers))


print(mean)
print(median)
print(mode)



