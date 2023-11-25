# Suppose a dictionary contains  5 key value pairs of name and marks . Write a program to print them from last to first. Keep deleting every pair printed, such that the end of printing the dictionary falls empty.

dictionary={
    "A":10,
    "B":20,
    "C":30,
    "D":40,
    "E":50
}
while dictionary:
    name,marks=dictionary.popitem()
    print(f"Name={name}")
    print(f"Marks={marks}")
print("Dictionary is now empty as asked!")