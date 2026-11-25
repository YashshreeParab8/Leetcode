#Q1 right rotate array
def rotateArray(arr):
    n=len(arr)
    if n==0:
        return arr
    r = r%n
    arr[:]=arr[-r:]+arr[:-r]
    return arr