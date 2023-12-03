# Write a program to illustrate the use of default values in a function’s definition.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Abc")  # Output: Hello, Abc!

greet("Xyz", "Hi")  # Output: Hi, Xyz!








# Write a program to find factorial of number. 

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(10))











# Write a program to find the maximum of two numbers.

def maximum(n1,n2):
    return max(n1,n2)
a=float(input("Enter first number>>"))
b=float(input("Enter second number>>"))

print(f"Maximum is {maximum(a,b)}")






# Write a program to show local scope vs global scope.
# Global variable

global_variable = "I am global"

def local_vs_global():
    # Local variable
    local_variable = "I am local"
    print(f"Inside the function: {global_variable}, {local_variable}")

local_vs_global()






# Write a program to access a local variable outside a function.

def function_with_local_variable():
    # Local variable
    local_variable = "I am local"
    return local_variable

local_variable = function_with_local_variable()

# Access and print the global variable
print(f"Outside the function: {local_variable}")






# Write a program using the global statement\n
# Global variable
global_variable = "I am global"

def modify_global_variable():
    # Use the global statement to indicate that we are modifying the global variable
    global global_variable
    # Modify the global variable
    global_variable = "Modified global value"
    print(f"Inside the function: {global_variable}")

# Call the function to modify the global variable
modify_global_variable()

# Access and print the modified global variable outside the function
print(f"Outside the function: {global_variable}")








# Write a program to return the minimum of two numbers.
def minimum(n1,n2):
    return min(n1,n2)
n1=float(input("Enter first number>>"))
n2=float(input("Enter second number>>"))
print(f"Minimum is {minimum(n1,n2)}")








# Write the function count_Letter(word, letter) which takes a word and a letter as arguments and returns the number of occurrences of that letter in the word.

def count_Letter(word, letter):
    return word.lower().count(letter.lower())

word=input("Enter word>>")
letter=input("Enter letter to find>>")

print(count_Letter(word,letter))








# A string contains a sequence of characters. Elements within a string can be accessed using an index which starts from 0. Write the function getChar(word, pos) which takes a word and a number as arguments and returns the character at that position. 

def letterAtPos(word,pos):
    return word[pos]
print("The letter at position 1 in Hey is",letterAtPos("Hey",1))














# Write a function Eliminate_Letter(word, letter) which takes a word and a letter as arguments and removes all the occurrences of that particular letter from the word. The function will return the remaining letters in the word. 

def Eliminate_Letter(word,letter):
    remaining=word.replace(letter,"")
    return remaining

print(Eliminate_Letter("Hey","e"))








# Write the function countVowels(word) which takes a word as an argument and returns the vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) in that word.

def countVowels(word):
    count=0
    vowels="aeiou"
    for i in word.lower():
        if i in vowels:
            count=count+1
    return count

print(countVowels("aeiou"))










# Write the function isReverse(word1, word2) which takes two words as arguments and returns True if the second word is the reverse of the first word.

def isReverse(word1,word2):
    return word1==word2[::-1]

print(isReverse("Hey","yeH"))











# Write a recursive function which computes the nth Fibonacci number.
def Fibonacci(n):
    if (n<=1):
        return n
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2))
print(Fibonacci(5))





# Calculate the factorial of a number using recursion.
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))







# For a quadratic equation in the form of ax2 +bx+c, the discriminant D, is b2  - 4ac. Write a
# function to compute the discriminant D, that returns the following output depending on the
# discriminant D.
# if D > 0: The Equation has two Real Roots
# if D = 0: The Equation has one Real Root
# if D < 0: The Equation has two Complex Roots

def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c

    # Output based on the discriminant value
    if discriminant > 0:
        return "The Equation has two Real Roots"
    elif discriminant == 0:
        return "The Equation has one Real Root"
    else:
        return "The Equation has two Complex Roots"

# Example usage:
a = 1
b = -3
c = 2

result = calculate_discriminant(a, b, c)
print(result)





# Write a program to pass the radius of a circle as a parameter to a function area_of_circle().
# Return the value none if the value of the radius is negative or return the area of the circle.

def area_of_circle(radius):
    if radius < 0:
        return None
    else:
        return 3.14 * radius ** 2

print(area_of_circle(5))  # Output: 78.53981633974483
print(area_of_circle(-5))  # Output: None






# Write a function calc_Distance(x1, y1, x2, y2) to calculate the distance between two points represented by Point1(x1, y1) and Point2 (x2, y2). 
import math

def calc_Distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(calc_Distance(5,6,7,8))


