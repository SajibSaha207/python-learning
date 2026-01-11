#1
numbers = [10, 20, 30, 40, 50]
print(numbers[0], numbers[-1])

#2
fruits = ["apple", "banana", "cherry"]
fruits[1] ="mango"
print(fruits)

#3
emptylist =[]
mylist=input("Enter your list: ")
emptylist.append(mylist)

print(emptylist)

#4 
colors = ["red", "blue", "green", "yellow"]
colors.remove("green")
print(colors)

#5
marks = [55, 67, 89, 45, 72]
i = 0
while i<len(marks):
    print(marks[i])
    i = i + 1

total_sum = sum(marks)
print(f"The sum of the marks is: {total_sum}")