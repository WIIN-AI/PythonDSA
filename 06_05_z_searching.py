list1 = [5, 8, 4, 6, 9, 2]

print(sorted(list1))
print(list1.index(9))
list1.append(9)
print(list1)
print(list1.count(9))


def search_liner(ls1: list, n: int) -> bool:
    i = 0

    while i < len(ls1):
        if ls1[i] == n:
            print("index",i,ls1[i])
            return True
        i = i + 1

    return False

l1 = [5, 8, 89, 100, 16]
target = 9

print(search_liner(l1, 9))

# binary search must be increasing order (lower bound and upper bound)
