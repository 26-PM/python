# Suppose a dictionary contains roll no  and names of students. @rite a program to receive the roll no extract the name corresponding to roll no and display a message congratulating student by his name. If the roll no doesn't exist in the dictionary, the message should be "Congratulations Student 
dictionary={
    1:"A",
    2:"B",
    3:"C",
    4:"D",
}
roll=int(input("Enter a roll number >> "))
studentName=dictionary.get(roll,None)
if studentName is not None:
    print(f"Congratulations {studentName}!")
else:
    print("Congratulations, student!")