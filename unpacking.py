# create 2 dictionaries called boys and girls containing names as keys and ages as values .
# Write a program to merge these 2 into a third dictionary using unpack operator.

dict1={"Boy1":16,"Boy2":17,}
dict2={"Girl1":15,"Girl2":16}

merge={**dict1,**dict2}
print("Merged Dictionary =",merge)