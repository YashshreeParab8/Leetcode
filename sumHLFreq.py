# given an array nums of n integer, calculate the sum of highest occuring number and lowest ocuuring number
def sumOfFrequencies(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    highest = max(count.values())
    lowest = min(count.values())
    return highest + lowest