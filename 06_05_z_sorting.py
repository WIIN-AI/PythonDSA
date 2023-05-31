# # bubble sort two pointer (i, j) o(n2) -
#
# ls1 = [5, 3, 8, 6, 7, 2]
# for i in range(len(ls1)):
#     for j in range(len(ls1) - i - 1):
#         if ls1[j] < ls1[j + 1]:
#             pass
#         else:
#             # temp = ls1[j]
#             # ls1[j] = ls1[j+1]
#             # ls1[j+1] = temp
#             ls1[j], ls1[j + 1] = ls1[j + 1], ls1[j]
#
# print(ls1)
#
# # selection sort - is finding the index of minimum value
# ls1 = [2, 3, 5, 6, 7, 8]
#
# for i in range(len(ls1)):
#     minpos = i
#     for j in range(i, len(ls1)):
#         if ls1[j] < ls1[minpos]:
#             minpos = j
#
#     temp = ls1[i]
#     ls1[i] = ls1[minpos]
#     ls1[minpos] = temp
#     print(ls1)
#
# print(ls1)
#
# # Miniumum also fine
# ls1 = [9, 3, 8, 6, 7, 2]
#
# # Miniumum also fine
# ls1 = [10, 3, 8, 6, 7, 2]
#
#
# def get_max_index(input_lst, start, end):
#     max_index = start
#     for index_ in range(end):
#         if input_lst[max_index] < input_lst[index_]:
#             max_index = i
#
#     return max_index
#
#
# def swap_values(inputs_lst, first_index, second_index):
#     temp = inputs_lst[first_index]
#     inputs_lst[first_index] = inputs_lst[second_index]
#     inputs_lst[second_index] = temp
#
#
# # ls3 = [10, 3, 8, 6, 7, 2]
# # # find the max element and swap
# # for i in range(len(ls3)):
# #     last = len(ls3) - i - 1
# #     max_index_val = get_max_index(ls3, start=0, end=last)
# #     print(max_index_val)
# #     print(ls3)
# #     swap_values(ls3, max_index_val, last)
# #
# # print(ls3)


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        # Find the index of the maximum element in the unsorted portion of the array
        max_index = i
        for j in range(i):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the maximum element with the last element in the unsorted portion of the array
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


arr = [10, 3, 8, 6, 7, 2]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 5, 6, 8]

# django-admin startproject publicview