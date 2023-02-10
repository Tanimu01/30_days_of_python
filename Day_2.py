#Day 2: 30 Days of python programming
first_name='Tanimu'
print(first_name)
last_name='Abdullahi'
print(last_name)
full_name='Tanimu Abdullahi'
print(full_name)
country_name='Nigeria'
print(country_name)
city_name='Kano'
print(city_name)
age=36
print(age)
year=1986
print(year)
is_married=True
print(is_married)
is_true=True
print(is_true)
is_light_on=False
print(is_light_on)
my_name,my_school,my_age,my_married_status='Tanimu Abdullahi','Bayero Univiersity Kano',36,True
print(my_name,my_school,my_age,my_married_status)

# Exercises: Level 2
print(type(first_name)) 
print(type(last_name))
print(type(full_name))
print(type(country_name))
print(type(city_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(my_name))
print(type(my_school))
print(type(my_age))
print(type(my_married_status))

print(len(first_name))
print("the maximum is ",max(len(first_name),len(last_name)))
print("the minimum is ",min(len(first_name),len(last_name)))

# Question 4 under Exercises: Level 2
num_one,num_two=5,4
total=num_one+num_two
print("the total is", total)
diff=num_two-num_one
print("the diff is", diff)
product=num_two*num_one
print("the product is",product)
division=num_one/num_two
print('the division is', division)
remainder=num_two%num_one
print("the remainder is", remainder)
exp=num_one**num_two
print("the exp is",exp)
floor_division=num_one//num_two
print("the floor_division is", floor_division)

import math
pi=math.pi
radius=30
area_of_circle=pi*radius**2
print("the area of circle is ", area_of_circle)
circum_of_circle=2*pi*radius
print("the circumference of the circle is", circum_of_circle)
nradius=int(input("enter the value of nradius"))
print(type(nradius))
new_area_of_circle=pi*nradius**2
print(" the new area of circle from user input is : ", new_area_of_circle)

first_name=input("enter your first name: ")
last_name=input("enter your last name: ")
country=input("enter your country name: ")
age=int(input("enter your age"))
print(first_name,last_name,country,age)
help('keywords')