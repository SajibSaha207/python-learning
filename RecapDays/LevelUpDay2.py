#1 Count how many numbers biger than 0

# 
# numbers = [-2, 5, 0, 3, -1, 8]
# count = 0

# for num in numbers:
#     if num > 0:
#      count += 1
# print(count)

#2 count vowel
text = "education"
vowel = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowel:
        count += 1
print(count)
        

#3 second leargest number

numbers = [10, 25, 5, 30, 20]

numbers = list(set(numbers))
if len(numbers)< 2:
    print("No 2nd largest number")
else:
    numbers.sort()
    print(numbers[-2])

