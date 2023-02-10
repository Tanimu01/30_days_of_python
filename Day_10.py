# Exercises: Level 1
# Q1 Iterate 0 to 10 using for loop, do the same using while loop.
count=0
while count<11:
    print(count)
    count=count+1
print('for loop print is')
for number in range(11):
    print(number)

# Q2 Iterate 10 to 0 using for loop, do the same using while loop.
count=0
while count<11:
    print(count)
    count=count+1
print('for loop print is')
for number in range(11):
    print(number)
    
di=10
while di>=0:
    print(di)
    di=di-1
for dinum in range(10,-1,-1):
    print(dinum)
# Q3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
x=0
while x<8:
 y=0
 while y<x:
        print('#', end='')
        y=y+1
 print(' ')
 x=x+1

 # Q4 Use nested loops to create the following:
 x=0
while x<7:
 y=0
 while y<8:
        print('#', end='')
        y=y+1
 print(' ')
 x=x+1
