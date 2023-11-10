my_list=[]
for i in range(6):
    number = int(input("Enter a number: "))
    my_list.append(number)

if((my_list[0]+my_list[1]+my_list[2])>(my_list[3]+my_list[2]+my_list[1])):
    my_list.sort()

print(my_list)
