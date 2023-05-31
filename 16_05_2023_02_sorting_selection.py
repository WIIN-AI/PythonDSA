"""Elementary Algorithm """
# Bubble sort -> N*N = n2 (worst case O(n^2), best case O(n), Average O(n^2))
# Selection sort ->  N*N = n2 (worst case O(n^2), best case O(n), Average O(n^2))
# Insertion sort
"""Advanced algorithm"""
# Merge Sort
# Quick Sort

"""Selection Sort"""


def selection_sort(arr: list):
    """
    step1 : two pointer
    step2 : set min_val_index to O and Swap the index if any other index found min by compare the index value LOOP 2
    Note : Each Iteration first index will be sorted
    Sorting One Element at time
    :param arr:
    :return:
    """
    for i in range(len(arr)):  # n
        min_val_index = i
        for j in range(i+1, len(arr)):  # n-1/2
            if arr[min_val_index] < arr[j]:
                pass
            else:
                min_val_index = j
        # temp = arr[i]
        # arr[i] = arr[min_val_index]
        # arr[min_val_index] = arr[i]
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]

    return arr


lst = [-2, 45, 6, 1, 11, -9]
results = selection_sort(lst)
print(results)

lst = [-2, -1, 1, 11]
results = selection_sort(lst)
print(results)
