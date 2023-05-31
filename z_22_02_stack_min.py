# Push - in
# Pop - out
# Peak - Top Value
"""
Push Means - add In
Pop Means - removing the FIRST (Zero) Index
Peak - Top of the value
"""
import sys


class MinStack:
    def __init__(self):
        self.lst = []
        self.min_stack = []
        self.min_val = sys.maxsize

    def push_in(self, val):
        self.lst.append(val)
        if val < self.min_val:
            self.min_val = val
            self.min_stack.append(self.min_val)

    def pop_out(self):
        val = self.lst.pop()
        print("pop_out", val)
        if val in self.min_stack:
            self.min_stack.remove(val)

    def console_log(self):
        print(self.lst)

    def get_min(self):
        print(self.min_val)
        print(self.min_stack)
        print("self.min_stack[-1]",self.min_stack[-2])


min_stack = MinStack()
min_stack.push_in(10)
min_stack.push_in(5)
min_stack.push_in(11)
min_stack.push_in(12)
min_stack.push_in(1)

min_stack.console_log()
min_stack.get_min()

min_stack.pop_out()
min_stack.get_min()



