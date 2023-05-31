

arr = [10,2,9,1,3,4,5]

n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            # temp = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+1] = temp
            arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

print(arr)