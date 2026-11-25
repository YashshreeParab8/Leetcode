#Q1 right rotate array
def rotateArray(arr):
    n=len(arr)
    if n==0:
        return arr
    r = r%n
    arr[:]=arr[-r:]+arr[:-r]
    return arr

# Q2 left rotate array
def rotateArray(arr, r: int):
    n = len(arr)
    if n == 0:
        return arr
    r = r%n
    arr[:]=arr[r:]+arr[:r]
    return arr

# Q3 duplicate zeros
def duplicateZeros(arr: list[int]) -> list[int]:
    result = []
    for i in arr:
        result.append(i)
        if i == 0:
            result.append(0)
    return result[:len(arr)]