# arr = [18, 19, 9, 14, 77, 50]
# target = 50
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)


# complexity O(1) - best case - which available in at first index
#            O(n) - worst case - which available in at last index


def linear_search_index(arr: list, target: int) -> int:
    if len(arr) > 0:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
    return -1  # no target found or no element in given array/list


def linear_search_return_bool(arr: list, target: int) -> bool:
    if len(arr) > 0:
        for i in range(len(arr)):
            if arr[i] == target:
                return True
    return False  # no target found or no element in given array/list


input_arr = [18, 19, 9, 14, 77, 50]
input_target = 1
output = linear_search_index(input_arr, input_target)
print(f"found at index {output}")

output = linear_search_return_bool(input_arr, input_target)
print(f"found at index {output}")
print("*" * 80)
## Search in strings


_str_name = "WIINAI KKUMAR"
_char_target = "B"


def linear_search_string(str_input: str, target) -> bool:
    # Note: In java, basically character variable defined as char
    # String defined as array only
    #
    if len(str_input) == 0: return False

    for i in range(len(str_input)):
        if str_input[i] == target:
            return True
    return False


output = linear_search_string(_str_name, _char_target)
print(output)


def find_minimum_number(arr: list, start: int, end: int) -> int:
    if len(arr) != 0:
        minimum = arr[0]
        for i in range(1, end):
            if arr[i] < minimum:
                minimum = arr[i]
        return minimum
    return -1


input_arr = [18, 19, 9, 14, 77, 50]
output = find_minimum_number(input_arr, start=0, end=len(input_arr))
print(f"minimum {output}")


# find minimum and maximum of given array

def find_minimum_max_number(arr: list, start: int, end: int) -> (int, int):
    if len(arr) != 0:
        minimum = arr[0]
        maximum = arr[0]
        for i in range(start, end):
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i] > maximum:
                maximum = arr[i]
        return minimum, maximum
    return -1


input_arr = [18, 19, 9, 14, 77, 50]
min_val, max_Val = find_minimum_max_number(input_arr, start=0, end=len(input_arr))
print(f"minimum {min_val, max_Val}")
print("min(input_arr)", min(input_arr))
print("max(input_arr)", max(input_arr))
print("#" * 80)

def find_min_max_in_2d_array(arr: list):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            print(arr[row][col])
            print(row, col)

    print("Second for each loop")
    for row_val in arr:
        for val in row_val:
            print(val)


input_arr = [
    [1, 10],
    [10, 12, 13]
]

find_min_max_in_2d_array(input_arr)


import sys
# Get the maximum integer value
max_int = sys.maxsize
# Get the minimum integer value
min_int = -sys.maxsize - 1
# Print the values
print(f"The maximum integer value is {max_int}")
print(f"The minimum integer value is {min_int}")


# Richest customer wealth

y = 2147395599


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x
        if x <= 3: return 1

        mid_val = int(x //2)
        for i in range(mid_val + 1):
            if i * i == int(x):
                return i
            else:
                if i * i > x:
                    return i - 1
        return i

print(Solution().mySqrt(y))
