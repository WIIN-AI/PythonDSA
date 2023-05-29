# Push - in
# Pop - out
# Peak - Top Value
"""
Push Means - add In
Pop Means - removing the FIRST (Zero) Index
Peak - Top of the value
"""
import sys


class MaxStack:
    def __init__(self):
        self.lst = []
        self.stack = []
        self.max_val = -sys.maxsize-1

    def push_in(self, val):
        self.lst.append(val)
        if val > self.max_val:
            self.max_val = val
            self.stack.append(self.max_val)

    def pop_out(self):
        val = self.lst.pop()
        print("pop_out", val)
        if val in self.stack:
            self.stack.remove(val)

    def console_log(self):
        print(self.lst)

    def get_max(self):
        print(self.max_val)
        print(self.stack)
        print("self.stack[-1]",self.stack[-1])


max_stack = MaxStack()
max_stack.push_in(10)
max_stack.push_in(5)
max_stack.push_in(11)
max_stack.push_in(12)
max_stack.push_in(1)

max_stack.console_log()
max_stack.get_max()

max_stack.pop_out()
max_stack.get_max()



