# insert element at given position and shift index
def  insertAtPosition(arr,X,P):
    N=len(arr)
    for i in range(N-1,P,-1):
        arr[i]=arr[i-1]
    arr[P]=X
    print(arr)
insertAtPosition([10,20,30,40],15,1)