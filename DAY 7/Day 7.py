# 1
numbers = [2, 4, 5, 2, 4, 6, 7, 5]
uni_numbers = set(numbers)
print("Uni_numbers: ", uni_numbers)
print("Total uni numbers: ", len(uni_numbers))

#2 
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
fruits.remove("banana")
print(fruits)

#3
class_A = {"Rahim", "Karim", "Sajib", "Hasan"}
class_B = {"Sajib", "Hasan", "Nafis"}

class_C = class_A.intersection(class_B)
class_C1 = class_A.difference(class_B)
print (class_C)
print(class_C1)

#4
marks = {55, 67, 89, 45, 72}
total_sum = 0
for mark in marks:
    print(mark)
    total_sum +=mark
print("The sum is :", total_sum)

#5
numbers = [1, 2, 3, 2, 4, 3]
new_set = set(numbers)
new_set = frozenset(numbers)
new_set.add(5) #nothing will be add in frozenset because frozenset is immutablr
print(new_set)
