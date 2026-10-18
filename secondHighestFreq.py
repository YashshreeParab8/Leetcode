# given an array nums of n integer, find the second most frequent occuring number in the array. if there are multiple 
# then return th smallest number, if second most does not exist then return -1
def secondHighestOccurringElement(arr):
    count={}
    for i in arr:
        if i in count:
            count[i] +=1
        else:
            count[i]=1
    freq = set(count.values())
    if len(freq)<2:
        return -1
    sec = sorted(freq, reverse = True)[1]
    result = None
    for i in count:
        if count[i]==sec:
            if result is None or i < result:
                result=i
    return result