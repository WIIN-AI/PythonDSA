# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A = sorted(A)
    old_lst = A.copy()
    highest_val= A[-1]
    while len(A) >=2 :
        if A[-1]-1 == A[-2]:
            A = A[:-2]
        else:
            highest_val = A[-1] - 1
            break

    if highest_val <= -1:
        return 1
    else:
        if highest_val in old_lst:
            return highest_val+1
        else:
            return highest_val






A = [-1,1,4,5]
print(solution(A))

import numpy as np
a =  {-1:np.array([
            [1,7],
            [2,8],
            [3,8]])
}