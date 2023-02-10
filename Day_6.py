# Exercises: Day 6
# Exercises : 1

# Q1
tp_1=()
print(tp_1)

# Q2
bro_1=('Ali','Ibrahim','Sani','sadeeq')
sis_1=('Aisha','Ummi','Zainab','Zahrau')
# Q3
siblings=bro_1+sis_1
print(siblings)

# Q4
len(siblings)
print(len(siblings))

# Q5
siblings=list(siblings)
f_m=['father','mother']
family_members=siblings+f_m
print(len(family_members))

# Exercises : 2
# Q1
sib_1,sib_2,sib_3,sib_4,sib_5,sib_6,sib_7,sib_8,*parents=family_members
print(parents)

# Q2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('mango','banana','apple')
vegetables=('tomoto', 'salad', 'onion')
animals=('cow','camel','goat')
food_stuff_tp=fruits+vegetables+animals
print(food_stuff_tp)

# Q3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list=list(food_stuff_tp)
print(food_stuff_tp)

# Q4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_mid=int(len(food_stuff_tp)/2)
print(food_stuff_tp[food_mid:])

# Q5 Slice out the first three items and the last three items from food_staff_lt list
food_stuff_list[3:]
food_stuff_list[:-3]

# Q6 Delete the food_staff_tp tuple completely
del food_stuff_tp

# Q7 Check if an item exists in tuple: Check if 'Estonia' is a nordic country ,Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)