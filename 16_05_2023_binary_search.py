def binary_search(input_arr: list, target: int) -> int:
    if len(input_arr) <= 0:
        return -1
    start = 0
    end = len(input_arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if input_arr[mid] == target:  # comparing the middle index value with target value
            return mid
        if target < input_arr[mid]:  # if middle index value is less than target value - shift the middle index to end
            end = mid - 1
        else:
            start = mid + 1

    return -1


lst = [1, 10, 12, 15, 16, 19]
print(binary_search(lst, 12))

lst1 = [1, 10, 12, 15, 16, 19]
print(binary_search(lst1, -1))
# log(n) = is time complexity
#
