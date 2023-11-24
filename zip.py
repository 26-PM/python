# WAP to create following 3 lists:
# A list of names, a list to roll numbers, a list of marks.
# Generate and print a list of tuples containing name, roll number, and marks from the 3 lists. From this list
# generate 3 tuples- one containing all names, another containing all roll numbers and third containing all
# marks.

list1=["Name1","Name2","Name3","Name4"]
list2=["RollNo.1","RollNo.2","RollNo.3","RollNo.4"]
list3=[10,20,30,40]
#packing
zipped=list(zip(list1,list2,list3))
print(zipped,"\n")
#unpacking
name,roll,marks=zip(*zipped)
print(tuple(name))
print(tuple(roll))
print(tuple(marks))
