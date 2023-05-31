def floor_of_number(arr: list, target: int) -> int:
    if len(arr) <= 0: return -1
    #     if target < arr[0] : return -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == target:
            return arr[mid]

        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return arr[end]


arr = [2, 3, 4, 5, 9, 14, 16, 17]
target = 1
print(floor_of_number(arr, target))