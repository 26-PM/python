sum=0
while True:
    number=int(input("Enter a number"))
    if (number==0):
        break;
    elif (number%2==0):
        sum=sum+number
print(sum)