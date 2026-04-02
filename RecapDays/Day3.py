#1
# from collections import Counter
# numbers = [1, 2, 2, 3, 1, 4, 2]

# frequency = Counter(numbers)
# print(dict(frequency))

#2 

# text = "programming"

# vowel ="aeiou"
# count_vowel= 0


# for char in text:
#     if char in vowel:
#         count_vowel += 1
# print (f"Vowel have: {count_vowel} times")

#3
# numbers = [1, 2, 3, 4, 5]
# reverse_numbers =[]

# for num in numbers:
#     reverse_numbers.insert(0,num)
# print(reverse_numbers)

#4
# marks = {
#     "Math": 85,
#     "English": 78,
#     "Physics": 92
# }

# highest_mark = 0
# highest_sub = ""

# for sub, mark in marks.items():
#     if mark > highest_mark:
#         highest_mark = mark
#         highest_sub = sub

# print(f"Highest mark is  {highest_sub}")

#5
# from collections import Counter
# numbers = [1, 2, 2, 3, 2]

# frequency = numbers.count(2)
# print(frequency)

#6
# numbers = [5, 10, 15, 20]
# count_even = 0

# for num in numbers:
#     if num % 2 == 0:
#         count_even += 1
# print(count_even)

#7
# numbers = [10, 25, 5, 30]
# smallest_number =10

# for num in numbers:
#     if smallest_number> num:
#         smallest_number = num
# print(f"min number is {smallest_number}")

#8
text = "hello"
count =0

for char in text:
    count += 1

print(count)