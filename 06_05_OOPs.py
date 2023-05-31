# In inheritance
class Student:
    def __init__(self, name, rollno, age=None):
        self.name = name
        self.rollno = rollno
        self.age = age

    def student_details(self):
        print(self.name, self.rollno)


s1 = Student("WIINAI KKUMAR", 7)
s1.student_details()


# Inheritance

class FeaturesDashboard:
    def __init__(self):
        self.params = "This is sample params PlaceHolder"

    def feature1(self):
        print(f"This is feature 1 function {self.params} ")

    def feature2(self):
        print(f"This is feature 2 function {self.params} ")


class Window1(FeaturesDashboard):

    def __init__(self):
        self.params = "This is sample params PlaceHolder"

    def feature3(self):
        print("This is feature 1 function ")

    def feature4(self):
        print("This is feature 2 function ")


# when you call it subclass it will look for first subclass constructor
# if we use the super() it will call A
# method resolution  of order (MRO) --> left to right call it __init__
# super() to call method from extended call

# ploymorphism - object take multiple form
# duck typing - >same method must be there  to send the object to send
# Operation Overloading
#

a = 10
b = 20
print(int.__add__(a, b))  # Magic method

print(type(a.__str__()))


# Method  Overloading (default parameters) -> None
# *vars
# Method overriding


class A:
    def show(self):
        print("Show A show")


class B(A):
    pass
    # def show(self):
    #     print("Show B show")


a1 = B()
a1.show()


# iterator
nums =[6,8,9]
# for i in nums: print(i)


numsIt = iter(nums)
# print(numsIt)
# print(numsIt.__next__())
# print(numsIt.__next__())
print(numsIt.__next__()) # Or
print(next(numsIt))
print(next(numsIt))

