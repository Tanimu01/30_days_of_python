# Exercises: Day 8

#  Q1 Create an empty dictionary called dog

dog={}
# Q2 Add name, color, breed, legs, age to the dog dictionary
dog={'name':'Tanimu Abdullahi', 'color':'red','breed':'chicken', 'legs':2,'age':36}
print(dog)

# Q3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dic={'first_name':'Tanimu ','last_name':'Abdullahi','gender':'male','age':36,'marital status':'married','skill':['C++','C','Java Script','python'],'country':'Nigeris','city':'kano','address':'hausawa sabon titi'}
print(student_dic)

# Q4 Get the length of the student dictionary
print(len(student_dic))

# Q5 Get the value of skills and check the data type, it should be a list
skil_list=student_dic['skill']
print(skil_list)
print(type(skil_list))

# Q6 Modify the skills values by adding one or two skills
n=len(student_dic['skill'])
student_dic['skill']='Sofware Development', "Sofware Maintenance",'Data Analysis'
print(student_dic['skill'])

# Q7 Get the dictionary keys as a list
student_dic.keys()
print(student_dic.keys())

# Q8 Get the dictionary values as a list
student_dic.values()
print(student_dic.values())

# Q9 Change the dictionary to a list of tuples using items() method
student_dic.items()
print(student_dic.items())

# Q10 Delete one of the items in the dictionary
student_dic.pop('skill')
print(student_dic)

# Q11 Delete one of the dictionaries
del student_dic