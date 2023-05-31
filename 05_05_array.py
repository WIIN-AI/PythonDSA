# no fix size


import array as arr

vals = arr.array('i',[5,8,10])
print(vals.buffer_info())


for i in vals:
    print(i)

print("*"*100)
for i in range(len(vals)):
    print(vals[i])


newArr = arr.array(vals.typecode, (a*a for a in vals))
print("newArr.index(10*10) at ",newArr.index(100) )
print(newArr)

vals = arr.array('u',["a","b"])
print(vals.buffer_info())
for i in vals:
    print(i)

vals.append("c")
print(vals)

val_input = input("Enter the input value -> ")
print(val_input)

