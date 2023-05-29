def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge_fn(left, right)


def merge_fn(left, right):
    new_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    new_arr = new_arr + left[i:]
    new_arr = new_arr + right[j:]
    return new_arr


lst1 = [1, 10, 12, 15, 16, 19,21,9]
new_lst = merge_sort(lst1)

print(lst1)
print(new_lst)
