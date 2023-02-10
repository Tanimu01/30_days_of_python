#  Exercises: Day 9
# Q1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
x=int(input('enter your age'))
if x>=18:
    print('You are old enough to drive')
else:
    y=18-x
    print('You need',y  ,'more years to learn to drive.')

# Q2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age=36
your_age=int(input('enter your age :'))
y=my_age-your_age

if my_age>your_age:
    if y==1:
        print('am',y, 'year older than you')
    else:
        print('am',y, 'years older than you')
else:
    xy=your_age-my_age
    if y==1:
        print('you are',xy, 'year older than me')
    else:
        print('you are',xy, 'years older than me')

# Q3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a=int(input('enter number 1 '))
b=int(input('enter number 2 '))

if a>b:
    print(a ,'is greater than',b)
elif a<b:
    print(a ,' is lesthan ',b)
    
else:
    print('a=b')

## Exercises: Level 2
# Q1 Write a code which gives grade to students according to theirs scores:
# 80-100, A 70-89, B 60-69, C 50-59, D 0-49, F
mark=int(input('enter mark'))
if mark>=80:
    print('A')
elif mark>=70:
    print('B')
elif mark>=60:
    print('C')
elif mark>=50:
    print('D')
else:
    print('F')

# Q2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month=input('enter the month')
if month=='September'or month=='October'or month=='November':
        print('the season is Autumn') 
elif month=='December'or month=='January'or month=='February':
        print('the season is Winter.') 
elif month=='March'or mark=='April'or mark=='May':
        print('the season is Spring')
else:
        print('the season is Summer')
# Q3 The following list contains some fruits: 
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'apple' in fruits:
  print('That fruit already exist in the list')
else:
    fruits.append('appple')
    print(fruits)


# Exercises: Level 3
# Q4 Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
if 'skills' in person:
  print(person['skills'])
  n=int(len(person['skills'])/2)
  print(n)
  print(person['skills'][n])

if 'Python' in person['skills']:
    print(person['skills'])
#  If a person skills has only JavaScript and React, print('He is a front end developer')
if person['skills']==['JavaScript','React']:
    print('He is a front end developer')
#if the person skills has Node, Python, MongoDB, print('He is a backend developer')
else:
    if ['Node','Python','MongoDB'] in person['skills']:
     print('He is a backend developer')
     #if the person skills has React, Node and MongoDB, Print('He is a fullstack developer')
    elif ['React','Node','MongoDB'] in person['skills']:
        print('He is a fullstack developer')
    else :
        print('unknown title')
#  If the person is married and if he lives in Finland, print the information in the following format:
if bool(person['is_marred']) and person['country']=='Finland':

    print(person['first_name'],person['last_name'],'lives in  ',person['country'],'. He is ', person['is_marred'])
