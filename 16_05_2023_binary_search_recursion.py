def binary_search(input_arr: list, target: int, start: int, end: int) -> int:
    if start > end:
        return -1

    mid = start + (end - start) // 2
    if input_arr[mid] == target:
        return mid
    elif target < input_arr[mid]:
        return binary_search(input_arr[start:mid - 1], target, start=start, end=mid - 1)
    else:
        return binary_search(input_arr[mid + 1:end], target, start=mid + 1, end=end)


lst = [1, 10, 12, 15, 16, 19]
print(binary_search(lst, 12, start=0, end=len(lst) - 1))

lst1 = [1, 10, 12, 15, 16, 19]
print(binary_search(lst1, -1, start=0, end=len(lst) - 1))
# log(n) = is time complexity
#
