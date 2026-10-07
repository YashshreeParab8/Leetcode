# Given a list of integers nums, return a new list with elements in reverse order without using 
# nums.reverse() or slicing nums[::-1].
#skilli practice question

def reverseList(nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)- 1,-1,-1):
        result.append(nums(i))
    return result