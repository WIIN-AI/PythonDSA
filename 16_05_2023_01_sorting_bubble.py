"""Elementary Algorithm """
# Bubble sort -> N*N = n2 (worst case O(n^2), best case O(n), Average O(n^2))
# Selection sort
# Insertion sort
"""Advanced algorithm"""
# Merge Sort
# Quick Sort

"""Bubble Sort"""


def bubble_sort(arr: list):
    swap_count = 0
    for i in range(len(arr)):  # n
        for j in range(len(arr) - i - 1):  # n-1/2
            if arr[j] < arr[j + 1]:
                pass
            else:
                # temp = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j + 1] = temp
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

        if swap_count == 0:
            print("list already sorted format")
            break

    return arr


lst = [-2, 45, 6, 1, 11, -9]
results = bubble_sort(lst)
print(results)

lst = [-2, -1, 1, 11]
results = bubble_sort(lst)
print(results)
