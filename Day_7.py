# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Q1 Find the length of the set it_companies
len(it_companies)
print(len(it_companies))

# Q2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Q3 Insert multiple IT companies at once to the set it_companies
multiple_itcomanies={'GTchart', 'Starlink','Telegram'}
multiple_itcomanies.update(it_companies)
print(multiple_itcomanies)

# Q4 Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# Q5 What is the difference between remove and discard
# Answer Remove returns an error if the item does not exit in the set while discard does not even if its not in the set

# Exercises: Level 2

# Q1 Join A and B iiii
C=A.union(B)
print(C)

# Q2 Find A intersection B
D=A.intersection(B)
print(D)

# Q3 Is A subset of B
E=A.issubset(B)
print(E)

# Q4 Are A and B disjoint sets
print(A.isdisjoint(B))

# Q5 Join A with B and B with A
print(A.union(B))
print(B.union(A))

# Q6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Exercises: Level 3
# Q1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print(age_set)
print(len(age))
print(len(age_set))
print(len(age)>len(age_set)) # age list is bigger

# Q2 Explain the difference between the following data types: string, list, tuple and set
# A string is a sequence of characters that can be a combination of letters, numbers, and special characters. It can be declared in python by using single quotes, double quotes, or even triple quotes
# Lists are one of the most powerful data structures in python. Lists are sequenced data types.  In Python, an empty list is created using list() function. They are just like the arrays declared in other languages. But the most powerful thing is that list need not be always homogeneous. A single list can contain strings, integers, as well as other objects. Lists can also be used for implementing stacks and queues. Lists are mutable, i.e., they can be altered once declared. The elements of list can be accessed using indexing and slicing operations
# Tuples in Python: A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception t0hat tuples cannot be changed once declared. Tuples are usually faster than lists.

# Q3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
word_s="I am a teacher and I love to inspire and teach people"
word_split=word_s.split()
word_len=len(word_split)
avg=int(word_len/2)
firs_split=word_split[:avg]
second_split=word_split[avg:]
first_set=set(firs_split)
secound_set=set(second_split)
print(first_set)
print(secound_set)
unique_word=first_set.symmetric_difference(secound_set) #symmetric_difference

print(unique_word) 
