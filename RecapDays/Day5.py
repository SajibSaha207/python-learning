#1
# numbers = [2, 7, 11, 15]
# target = 9

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#              print(i,j) 

#2

# numbers = [1, 2, 3, 4, 5]

# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append(num * num)
#     else:
#         result.append(num)
# print(result)

#3
# text = "hello world"
# frequency={}

# for char in text:
#     if not char.isspace():
#         frequency[char] = frequency.get(char, 0) +1
# print(frequency)

#4
# from collections import Counter
# numbers = [1, 2, 2, 3, 3, 4]

# count = Counter(numbers)

# res = [num for num, freq in count.items() if freq > 1]
# print(res)

# numbers = [2, 7, 11, 15]
# target = 9

# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] + numbers[j] == target:
#          print(target)


numbers = [1, 2, 3, 4, 5]

result=[]
for num in numbers:
    if num % 2 == 0:
        result.append(num * num)
    else:
        result.append(num)
print(result)