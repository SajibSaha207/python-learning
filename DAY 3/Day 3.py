# p 1
a = input("Enter your number: ")
b = input("Enter your number: ")

sum = int(a) + int(b)
print ("The sum is: ", sum)

diff = int(a) - int(b)
print("The difference is: ", diff)

mult = int(a) * int(b)
print("The multiplication is: ", mult)

div = int(a) / int(b)
print("The division is: ", div) 

# p 2

a = input("Enter the number: ")
b = input("Enter the 2nd number: ")

if(a > b):
    print(True)
elif(a == b):
    print(False)
else:
    print(True)

# p 3
x = input("Enter your age: ")

if(x >= 18):
    print("Age is valid for voting")
else:
    print("Age is not valid for voting")

# p 4

text = "python programming"

print("python" in text)
print ("java" not in text)

# p 5

result = 10 + 5 * 2 ** 2
print(result)