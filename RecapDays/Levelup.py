#1
# from collections import Counter
# numbers = [1, 2, 2, 3, 3, 4]

# count = Counter(numbers)
# res =[num for num, frq in count.items() if frq > 1 ]
# print(res)

#2
# numbers = [10, 25, 5, 30]
# smallest=10
# for num in numbers:
#     if num<smallest:
#         smallest=num
# print(smallest)



#
numbers = [1, 2, 2, 3, 3, 4]

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
         if numbers [i] == numbers [j]:
              count += 1
    
    if count > 1:
         print(numbers[i])

# for j in range(len(numbers)):
#     if numbers[i] == numbers[j]:
#           count += 1

# if count > 1:
#     print(numbers[i])

