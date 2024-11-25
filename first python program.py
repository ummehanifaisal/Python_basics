# printing.........................................

print("Hello World")
print("Hello me hani","My age is 19")
print(23)
print(23+35)

# variable.........................................

# var = value
name = "hani"  #string
price = 29.54  

print("My name is :", name , "Price is :", price)
print(type(name))

age = 23
old = False
a = None
print(type(old))
print(type(a))

# print sum
a = 2
b = 4
sum = a + b
print(sum)

# taking input from user and printing it
"""hname = input("name: ")
hage = input("age: ")
hprice = input("price: ")

print(hname, hage, hprice)"""

#operators

#type casting

a,b = 3,"2"
c = int(b)
sum = a+c
print(sum)

# strings

str1 = "first string\n"
str2 = 'second string\n'
str3 = """three ways to
write string"""

# for concatenation
print (str1 + str2 + str3)

# for finding length
print(len(str1))

# Slicing
str = "coding"
print( str[1:4])
print(str[1: len(str)])

statement = "i am coder"
print(statement.capitalize())
print(statement.endswith("ee"))
print(statement.find("am"))
print(statement.count("o"))
print(statement.replace("e","r"))

 # WAP to check if the number entered by user is oddor even

"""number = int(input("Enter a number: "))
if(number%2 == 0):
    print("Number is even")
else:
    print("Number is odd")"""

# WAP to find the greatest of three numbers entered by user
    
"""n1 = int(input("enter first num: "))
n2 = int(input("enter second num: "))
n3 = int(input("enter third num: "))

print("The greatest number is:")
if(n1>=n2 and n1>=n3):
    print(n1)
elif(n2>=n3):
    print(n2)
else:
    print(n3)"""

# WAP to check if the number is multiple of 7 or not

"""num1 = int(input("enter a number: "))
if(num1 % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")"""


# lists and tuples
    
"""mark = [34, 24, 40, 28]
print(mark)
print(mark[3])
mark[1] = 35
print(mark[1])
print(mark[1:len(mark)])"""


# Loops in python

#print no 1 to 50
"""i = 1
while i<= 50 :
    print(i)
    i+=1"""

#print no 100 to 1
"""i = 100
while i >= 1 :
    print(i)
    i-=1"""

#print a multiplication table of number n.
"""n = int(input("Enter a number: ")) 
i = 1
while i<=10:
    print(n , "*" , i , "=" , n * i )
    i+=1"""

#print the elements of the following list using a table
# [1,4,9,16,25,36,49,64,81,100]
    
"""i = 1
while i <= 10:
    print(i*i)
    i+=1"""

# OR
    
"""nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1"""

# search for a num x in tuple
no = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nn = int(input("Enter a number to search: "))
i = 0
found = False  # Add a flag to track if the number is found or not
while i < len(no):
    if no[i] == nn:
        print("Found at index", i)
        found = True  # Set the flag to True if the number is found
        break  # Exit the loop once the number is found
    i += 1

if not found:  # If the number is not found, print a message
    print("Number not found.")
    
# WAP to print sum of natural no.s n

noo = 7  # 1 se 7 tk sare numbers ka sum
sum = 0
i = 1

while i<=noo :
    sum+=i
    i+=1

    print("Total sum = ", sum)

# WAP to print factorial of n num
    
no1 = 5  # 1 se 7 tk sare numbers ka sum
factorial = 1
i = 1

while i <= no1 :
    factorial *= i
    i+=1

    print("factorial of n = ", factorial)