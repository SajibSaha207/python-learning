# my_array = [7, 12, 9, 4, 11]
# minVlue = my_array[0]

# for i in my_array:
#     if i < minVlue:
#         minVlue = i

# print('The lowest value: ',minVlue)

# 1
# arr = [10, 20, 30, 40, 50]
# for num in arr:
#     print(num)

#2 Find even index
arr = [5, 10, 15, 20]

for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])

# #3 largest number
# arr = [3, 7, 2, 9, 5]
# lar_num = arr[0]
# for i in arr:
#     if i > lar_num:
#         lar_num = i
# print('The largest number: ', lar_num)


# Recap

#1 make a another list for even number
# arr = [1, 2, 3, 4, 5]
# even_num = []

# for num in arr:
#     if num % 2 == 0:
#         even_num.append(num)
# print(even_num)

#2 check every number is even
arr = [2, 4, 6, 8, 10]

all_even = "true"

for num in arr:
    if num % 2 != 0:
        all_even = False
print(all_even)
