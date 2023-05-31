
def person(*var ,**kargs):
    for i in var:
        print(i)

    for i ,j in kargs.items():
        print(i ,j)



person(10, name = "WIINAI")

def fib(n):

    if n ==1 :
        print(0)
    else:
        a = 0
        b = 1
        for i in range(0 ,n):
            c = a+ b
            a = b
            b = c
            print(c)


# fib(5)

def fact(n):
    # # f = 1
    # # for i in range(1,n+1):
    # #     f = f*i
    #
    # print(f)
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(5))

#  function calling itself called as recurssion

# single time expression
f = lambda a: a * a
print(f(4))

# single time expression
ff2 = lambda a, b: a * b
print(ff2(4, 2))

nums = [2, 3, 4, 5, 6, 7, 8, 9]


def is_even(n):
    return n % 2 == 0


evens = list(filter(is_even, nums))
print(evens)

# lambda
evens = list(filter(lambda n: n%2==0, nums))
print(evens)


#double the

double_even = list(map(lambda n: n*2, evens))
print(double_even)

a =10
b =20

a,b = b,a
print(a,b)