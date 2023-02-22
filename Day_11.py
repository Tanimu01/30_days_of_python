# Exercises: Day 11
# Q1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sumf(x,y):
    sum=x+y
    return sum
print(sumf(7,5))
# Q2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(f):
    pi=3.142
    areaofcircle=pi*f*f
    return areaofcircle
print(area_circle(2))

# Q3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.