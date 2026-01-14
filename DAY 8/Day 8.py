#1
# student = {
#     "name": "Sajib",
#     "age": 22,
#     "department": "CSE"
# }
# print(student["name"])
# student["age"]= 23
# print(student["age"])
# print(student)

#2
# car = {
#     "brand": "Toyota",
#     "model": "Corolla",
#     "year": 2020
# }
# car["color"]= "white"
# print(car)
# car.pop("year")
# print(car)

#3

marks = {
    "Math": 85,
    "English": 78,
    "Physics": 92
}

for sub in marks:
    print(sub)
for mark in marks.values():
    print(mark)

total_sum = 0
# for mark in marks:
total_sum += mark
print(f"Total_sum: {total_sum}")
