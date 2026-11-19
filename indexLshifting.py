# left shifting
def leftShift(arr, K):
    N=len(arr)
    for i in range(N-K):
        arr[i]=arr[i+K]
    start=max(0,N-K)
    for i in range(start,N):
        arr[i]=0
    print(arr)
leftShift([10,20,30,40],2)