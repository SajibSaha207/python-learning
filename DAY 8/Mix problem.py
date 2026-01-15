#1
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

# total_sum = num1 + num2
# print(total_sum)

# total_diff = num1 - num2
# print(total_diff)

# total_mul = num1 * num2
# print(total_mul)

# total_div = num1 / num2
# print(total_div)

#2
# num = int(input("Enter your  number: "))

# if num >= 0:
#     print("Positive")
# elif num <= 0:
#     print("Negative")
# else:
#     print("Number is zero")

#3
# numbers = [12, 45, 7, 89, 23]
# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))

#4
# marks = [55, 67, 89, 45, 72]

# for mark in marks:
#     if mark > 60:
#         print("Marks is: ", mark)

# total_sum = sum(marks)
# print(total_sum)

#5
# from collections import Counter
# nums = [1, 2, 3, 2, 4, 2, 5]

# frequency = Counter(2)
# print(frequency)

#6
# student = ("Rahim", 21, "CSE")
# (Name, Age, Dept) = student
# print("name: ",Name)
# print("age: ",Age)
# print("dept: ",Dept)

#7

# numbers = [2, 4, 5, 2, 4, 6, 7, 5]
# uni_numbers = set(numbers)

# print("Uni_numbers: ", uni_numbers)
# print("Total Uni_numbers: ", len(uni_numbers))

# 8
# student = {
#   "name": "Sajib",
#   "age": 22,
#   "dept": "CSE"
# }
# print(student["name"])
# student["age"]= 23
# print(student)

#9
# marks = {
#   "Math": 85,
#   "English": 78,
#   "Physics": 92
# }
# total_sum=0
# for sub in marks:
#     print(sub)
# for mark in marks.values():
#     total_sum += mark
# print(f"Total_Sum:{total_sum} ")

#10
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)