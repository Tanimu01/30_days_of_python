# Q1 Explain the difference between map, filter, and reduce.
# Map: returns an array of pieces of information from the original array. In the callback function, return the data you wish to be part of the new array.
# Filter: returns a subset of the original array based on custom criteria. In your callback function, return a boolean value to determine whether or not each item will be included in the new array.
# Reduce: can be used to return almost anything. It is often used to return a single number, like an sum, but it can also be used to combine the logic of Map and Filter to return an array of values matching certain criteria. This can remove unnecessary iterations.
 
# Q2 Explain the difference between higher order function, closure and decorator
# A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as a parameter or returns a function as a result
# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed
# Decorators: are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# Q3 Define a call function before map, filter or reduce, see examples
# The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
#

# Q4 Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for i in countries:
     print(i)

# Q5 Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for j in names:
     print(j)

# Q6 Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for k in numbers:
     print(k)

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
# Q7 Use map to create a new list by changing each country to uppercase in the countries list
def to_upper(x):
     y=x.upper()
     return y
coun_upper = map(to_upper, countries)
print(list(coun_upper)) 

# Q8 Use map to create a new list by changing each number to its square in the numbers list
def squre(x):
     s=x*x
     return s
square_list=map(square,numbers)
print(list(square_list))

# Q9 Use map to change each name to uppercase in the names list
name_upper=map(to_upper,names)
print(list(name_upper))

# Q10 Use filter to filter out countries containing 'land'.
def fland(x):
     if 'land' in x:
          return True
     return False

k=filter(fland,countries)
print(list(k))

# Q11 Use filter to filter out countries having exactly six characters.

       

