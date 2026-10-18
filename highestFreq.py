# given an array nums of n integer, find the most frequent occuring numberin the array. if there are multiple 
# then return th smallest number
def highestOccurringElement(nums):
    count = {}
    
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    max = 0
    result = nums[0]
    for i in count:
        if count[i]>max:
            max = count[i]
            result = i
        elif count[i] == max and i < result:
            result = 1
    return result