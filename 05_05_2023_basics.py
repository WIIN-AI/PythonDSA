# tuple1 = (1, 2, 3, 4, 5)
# array1 = [1, 3, 4, 10, 5, 5, 5, ]
# set1 = {1, 3, 4, 4, 4}  # why set is not allow the duplicate values ? why can't we access set with Index
# # when you print it, it will print only unique values
#
#
# # print(set1[1]) # TypeError: 'set' object is not subscriptable - this is unorder
#
# from datetime import date
#
#
# class SampleClass:
#     sampleClassCounter = 0
#
#     def __init__(self, name=None, age=None):  # this constructor
#         print("This is constructor ")
#         self.name = "NAME"
#         self.age = 23
#         SampleClass.sampleClassCounter += 1
#
#     @classmethod
#     def class_method(cls, name, birth_year):
#         print("this is class method")
#         return cls(name, age=date.today().year - birth_year)
#
#     @staticmethod
#     def sample_static_method():
#         print("this is sample static method")
#
#     def sample_class_function_method(self):
#         print("this is sample class based function call")
#         print("self.name, self.age -> current values ", self.name, self.age)
#
#         # by default return None
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_age(self, age):
#         self.age = age
#
#
# sampleclass = SampleClass()
#
# print("cls counter", SampleClass.sampleClassCounter)
# sampleclass.set_name("WIINAI KKUMAR")
# sampleclass.set_age(100)
#
# print(sampleclass.sample_class_function_method())
# print("cls counter after class initialization ", SampleClass.sampleClassCounter)
# print(isinstance(sampleclass, SampleClass))
#
# values = [1, 10, 12, 14, 15, 17]
# for val in values: print(val)
#
# # find the index 10
# target = 19
# target_status = False
#
# for _index in range(len(values)):
#     if values[_index] == target:
#         target_status = True
#         print(f"{target} index at {_index}")
#         break
#
# print("target_status", target_status)
#
# target = 17
# start = 0
# end = len(values) - 1
# target_status = False
#
# while start <= end:
#     print("start, end", start, end)
#     mid = start + (end - start) // 2
#     print("mid", mid)
#     if values[mid] == target:
#         print(f"found the target..at {mid}")
#         target_status = True
#         break
#
#     if values[mid] < target :
#         start = mid + 1
#     else:
#         end = mid -1
#
# print("target_status", target_status)
#
# # Lists, Recursion, Stacks, Queues
# # Doubly Linked List
# # Circular Doubly Linked List
# # searching
# # Trees / Binary trees
# # Binary Search Trees
# # bubble / insertion /
#
#
# factorial(int n) {
# if ( n == 0 ) return 1
# return n*factorial(n-1)
# }
#
# F(int n) {
# if ( n == 0 ) return 0
# if ( n == 1 ) return 1
# return F(n-1) + F(n-2)
# }
#
# #bubble
# for ( i = 1 ; i < n ; i++ )
#     for ( j = n-1 ; j >= i ; j-- )
#         if ( a[j] < a[j-1] )
#             swap a[j] and a[j-1]
#
#
# # insertion
#
# for ( i = 1 ; i < n ; i++ ) {
#     j = i
#     t = a[j]
#     while ( j > 0 && t < a[j-1] ) {
#         a[j] = a[j-1]
#         j--
#     }
#     a[j] = t
# }
#
# # Selection Sort
# for ( i = 0 ; i < n-1 ; i++ ) {
#     k = i
#     for ( j = i+1 ; j < n ; j++ )
#         if ( a[j] < a[k] )
#             k = j
#             swap a[i] and a[k]
# }
#
# # Quicksort Sub-array is the standard Quicksort strategy (pivot) split left half and right half
# #  Mergesort divide and conquer sorting strategy O(nlog2 n).
# mergesort(array a, int left, int right) {
#     if ( left < right ) {
#         mid = (left + right) / 2
#         mergesort(a, left, mid)
#         mergesort(a, mid+1, right)
#         merge(a, left, mid, right)
#     }
# }
#
# merge(array a, int left, int mid, int right) {
#     create new array b of size right-left+1
#     bcount = 0
#     lcount = left
#     rcount = mid+1
#     while ( (lcount <= mid) and (rcount <= right) ) {
#         if ( a[lcount] <= a[rcount] )
#         b[bcount++] = a[lcount++]
#         else
#         b[bcount++] = a[rcount++]
#     }
#     if ( lcount > mid )
#         while ( rcount <= right )
#             b[bcount++] = a[rcount++]
#     else
#         while ( lcount <= mid )
#             b[bcount++] = a[lcount++]
#     for ( bcount = 0 ; bcount < right-left+1 ; bcount++ )
#         a[left+bcount] = b[bcount]
# }
#
# #hashing/ double hashing
# # graphs
# #  Shortest paths – Dijkstra’s algorithm
# #  Shortest paths – Floyd’s algorithm
# #  Minimal spanning trees