from array import *
def rotate(arr, n):
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
        arr[0] = x
        return arr


n = int(input())
for i in range(n):
        arr1 = list(map(int,input().split(' ')))
print(rotate(arr1,n))