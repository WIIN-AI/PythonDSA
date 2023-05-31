a = list()
given_list = [1,3,4,5,6,7,8,9]
target = 7
end = len(given_list)-1

start = 0
while start <= end:
    mid = (start + end -1)//2
    if given_list[mid] == target:
        print(1)
        print(mid)
        break

    if given_list[mid] < target:
        start = mid+1
    else:
        end = start +1


####################################################

