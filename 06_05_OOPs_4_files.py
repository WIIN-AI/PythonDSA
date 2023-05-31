data_input= """
This is text file input
this only purpose to create a file 
just open a file 
close the file 
delete file a 
"""

f1=open("mydata1","w") # Check and create
f1.write(data_input)
f1.close()
# print(f.read())


f1=open("mydata","a") # Check and create
f1.write(data_input)
f1.close()

f = open("mydata","r") # or 'rb' - read binary format
print(f.read())

# print(f.readline(3))