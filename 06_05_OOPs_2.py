class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
print(next(values))  # iteration
for i in values: print(i)


def top_ten_values():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def topten():
     n =1
     while n<=10:
         sq = n*n
         yield sq
         n +=1



values = top_ten_values()
print(values)
print(values.__next__())
for i in values: print(i)

values = topten()
print(values)
print(values.__next__())
for i in values: print(i)


a = 10
b = 20
try:
    print("logic started ")
    print(a/b)
    # print("logic closed ")
except ValueError :
    print("invalid input")
except ZeroDivisionError:
    print("Divided by Zero is not possible")
except Exception as e :
    print("Division is having some error",e)
finally:
    a = None
    b = None
    print("logic closed ")

print("hello....")