# # right index shifting by 3 (for right shiftinng start pointer from right side)
arr=[5,10,15,20,25,30,35]
pos = 3
for i in range(len(arr)-1,pos-1,-1):
    arr[i]=arr[i-pos]
for i in range (pos):
    arr[i]=0
print(arr)

# left index shifting
arr=[5,10,15,20,25,30]
pos = 1
for i in range(len(arr)-pos):
    arr[i]=arr[i+pos]
for i in range (-1,pos-1):
    arr[i]=0
print(arr)

arr=[5,10,15,20,25,30]
pos = 3
# for i in range (-1,pos):
#     arr[i]=0
# print(arr)

arr=[5,10,20,25]
pos=2
num=15
for i in range(pos,len(arr)):
    len(arr)-1
print(arr)