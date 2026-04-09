#1
# numbers = [1, 3, 5, 2, 8, 6]

# even_number =[]

# for num in numbers:
#     if num % 2 == 0:
#         even_number.append(num)
# print(even_number)

#2
# numbers = [10, 20, 30, 40]

# for num in numbers:
#     total_sum = sum(numbers)
# avg = total_sum / len(numbers)
# print(avg)

#3
# from collections import Counter
# text = "banana"
# count = 0

# for ch in text:
#     if ch == "a":
#         count += 1

# print(count)
#4
numbers = [2, 4, 6, 8,1]

all_even = True

for num in numbers:
    if num % 2 != 0:
        all_even = False

if all_even:
    print("All numbers are even")
else:
    print("Not all numbers are even")