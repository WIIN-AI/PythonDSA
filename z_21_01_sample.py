arr = [1, 2, 4, 6, 7, 9]
sum_val = 8

lower = 0
higher = len(arr) - 1  # max value index if it sorted array

pair_sum_lst = []

while lower < higher:
    if arr[lower] + arr[higher] == sum_val:
        pair_sum_lst.append([lower, higher])
        lower += 1
        higher -= 1
    elif arr[higher] >= sum_val or arr[lower] + arr[higher] > sum_val:
        higher -= 1
    else:
        lower += 1

print(pair_sum_lst)

pair_sum_lst = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == sum_val:
            pair_sum_lst.append([arr[i], arr[j]])


print(pair_sum_lst)