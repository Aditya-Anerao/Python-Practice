first_name = "Aditya"
last_name = "Anerao"
full_name = first_name + " " + last_name
print(full_name)

name = input("What is your name? ")
print("Hello", name)


birth_year = input("Enter your birth year: ")
age = 2021 - int(birth_year)
print("Age = ", age)


""" Value Type Conversions
str() --> string
int() --> integer ex: 10
float() --> decimal ex: 10.1
bool() --> boolean

"""

#Calculator Program
V1 = input("Value 1: ")
V2 = float(input("Value 2: "))
Sum = float(V1) + V2
print("Sum: ", Sum)

course = 'Python for Beginners'
print(course.upper())

Temp = float(input("What is the temparature? "))
if Temp > 80:
    print("It's a hot today")
    print("please hydrate")
elif Temp > 60: #(20, 30]
    print("It's a nice day")
else:
    print("It is cold")


#Weight Converter
Raw_data = float(input("Weight: "))
Units = input("(K)g or (L)bs: ")
if Units.upper() == "K":
    Weight = Raw_data / 0.45
    print ("Weight in LBs: ", Weight)
elif Units.upper() == "L":
    Weight = Raw_data * 2.2
    print ("Weight in KG:", Weight)
else:
    print("Invalid Units Entered")

i = 1
while i<=3:
    print (i * " *")
    i += 1
while i>= 1:
    print (i * ' *')
    i -= 1

friends = ['DK','Sanjeev', 'Meepy', 'Shanny', 'Mohit', "Abhi"]
friends.insert(3,"Adi")
if "Abhi" in friends:
    friends.remove("Abhi")
print ("I have ", len(friends)-1, " friends!")
#for loop version
for homie in friends:
    print(homie)
i=0
#while loop version
while i < len(friends):
    print(friends[i])
    i+=1

print("Friend List = ", friends[0:6])
#lists --> [inclusive:exclusive)


numbers = range(1,11,2) #lists --> [inclusive lowerBound, exclusive upperBound, step)
for number in numbers:
    print(number)