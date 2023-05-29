arr = [1, 2, 4, 6, 7, 9]

# Two Sum
# list
# Hash Map


nums = [2, 7, 11, 15];
target = 18
result = []

for _index in range(len(nums)):
    for _outerIndex in range(_index + 1, len(nums)):
        if nums[_index] + nums[_outerIndex] == target:
            result.append([_index, _outerIndex])

print(result)

result = []

hast_tbl = {"val":"index"}
for index in range(len(nums)):
    if nums[index] in hast_tbl.keys() :
        result.append([hast_tbl[nums[index]],index])
    else:
        hast_tbl[target-nums[index]]=index

print(result)
