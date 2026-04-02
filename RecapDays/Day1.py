#1

# numbers = [10, 20, 30, 40]

# for number in numbers:
#     total_sum = sum(numbers)
# print(total_sum)

# numbers = [5, 10, 15]
# total_sum =0

# for num in numbers:
#     total_sum +=num
# print(total_sum)


#2

# def count_even_numbers(numbers):
#     even_count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             even_count += 1
#     return even_count

# numbers = [1, 2, 3, 4, 5, 6]
# frequency = count_even_numbers(numbers)
# print(f"The frequency of even numbers is: {frequency}")

#3
# num = int(input("Enter The number: "))

# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     num=0
#     print("ZERO")

    

numbers = [2, 3, 4]
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    
print(even_count)




