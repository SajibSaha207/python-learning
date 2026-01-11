x = input()
y = input()
z = input()

a = float(x)
b = float(y)
c = float(z)

count = 3

total= (a + b + c)

average = total/ count

print(average)

#p2
a = 10
b = 15
c = 11

a,b,c = b,c,a
print(b,c,a)

#p3
a = 10
b = 15
c = 11

if(a<b and a<c):
    print("smallest number is: ", a)
elif(b<a and b<c):
    print("smallest number is: ", b)
else:
    print("smallest number is: ",c)


#p4
my_value = input()
result = my_value.isdigit()
print(result)


#p 5
a = 3.5e4

print("Float value is:" ,float(a))
print("Integer value is:" ,int(a))