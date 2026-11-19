# right index shifting
def rightShift(arr,K):
    N=len(arr)
    K=min(K,N)
    for i in range(N-1,K-1,-1):
        arr[i]=arr[i-K]
    for i in range(K):
        arr[i]=0
    print(arr)
rightShift([10,20,30,40],2)