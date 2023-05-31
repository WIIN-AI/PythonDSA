def quick_sort(arr, start, end):
    # base case
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1
        if arr[pivot] <= arr[right]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

    return arr


lst1 = [1, 10, 12, 15, 16, 19, 21, 9]
new_lst = quick_sort(lst1, start=0, end=len(lst1)-1)

print(lst1)
print(new_lst)
