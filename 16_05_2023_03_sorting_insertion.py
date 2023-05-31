"""Elementary Algorithm """
# Bubble sort -> N*N = n2 (worst case O(n^2), best case O(n), Average O(n^2))
# Selection sort
# Insertion sort
"""Advanced algorithm"""
# Merge Sort
# Quick Sort

"""Insertion Sort"""


def insertion_sort(arr: list):
    # for i in range(0, len(arr) - 1):
    #     j = i + 1
    #     while j > 0:
    #         if arr[j] > arr[j - 1]:
    #             break
    #         else:
    #             arr[j], arr[j - 1] = arr[j - 1], arr[j]
    #         j -= 1
    # return arr
    #

    for i in range(len(arr) - 1):
        for j in range(i+1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


lst = [-2, 45, 6, 1, 11, -9]
results = insertion_sort(lst)
print(results)

lst = [-2, -1, 1, 11]
# results = insertion_sort(lst)
# print(results)

# for i in range(1, len(lst)-2):
#     j = i + 1
#     while j > 0:
#         if lst[j] > lst[j - 1]:
#             pass
#         else:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
#         j -= 1
#
# print(lst)
