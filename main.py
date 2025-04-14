# Task 1
name = "Sheikh Radin"
age = 20 
student = True

print(type(name))
print(type(age))
print(type(student))

# Task 2

add = age + 5
sub = age - 10
multiply = age * 7 
division = age/3

print(add)
print(sub)
print(multiply)
print(division)

# Task 3

if age == 18:
    print("you are 18 years old")

if age > 18:
    print("Your age is greater than 18")
if age != 18:
    print("you are not 18 years old")

# Task 4
a = 5
b = 10
c = 15

if a < b and b < c:
    print("B is greater than A but C is greater than B ")

if a == b or a < b :
    print("A is equal or smaller than B")
if not(a > b and b > c ):
    print("B is greater than A and C")

# Task 5

num = 6
num +=5
print(num)
num -= 3
print(num)
num *= 8
print(num)
num /= 16
print(num)

# Task 6

num = 9
n = 0

print(n is num)

print(n is not num)

numbers = [1,3,556,2]
numbers2 = [2,4,5,67]
cnum = numbers
print(numbers is numbers2)
print(numbers is not numbers2)
print(numbers is cnum)
print(numbers is not cnum)

# Task 7
cars = ['BMW','Toyota','Ferrari']

if "BMW" in cars:
    print('BMW is available')

if "Bugati" not in cars:
    print("Bugati is not here")

if "Ferrari" not in cars:
    print('Ferrari is not here')