x = 'awesome'

def myfunc():
    x = "Good Morning"
    print("Python is " + x) 

myfunc()
# print("Python is" + x)

# #P 1
x = 7.5
print(f"{x} is of type {type(x)}")

# #p 2
a = 5e2
b = 3E3
c = -9.1e1
print(a, b, c)
print(type(a), type(b), type(c))

# #p 3
x = input("Enter a number: ")
a = int(x)

print(f"Number is:{a} and its type is: {type(a)}" )

# #p 4
x = 9.99
a = int(x)
print(a)

# #p5

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

sum= int (a) + int (b)  

print (sum)

#6
x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")
z = input("Enter 3rd number: ")

a = float(x)
b = float (y)
c = float (z)

if a>b and a>c :
    print("Largest number is:", a)
elif b>a and b>c :
    print("Largest number is:", b)
else :
    print("Largest number is:", c)


