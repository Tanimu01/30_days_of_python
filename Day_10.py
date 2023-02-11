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
y=0
while x<8:
 
 while y<8:
        print('x ', end='')
        y=y+1
 print(' ')
 x=x+1
 y=0
 # Q5 Print the following pattern:
 m=0
 while m<10:
    print(m,'X',m,'=',m*m)
    m=m+1

# Q6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list_it=['Python', 'Numpy','Pandas','Django', 'Flask']
n=len(list_it)
for i in range(0,n,1):
    print(list_it[i])

# Q7 Use for loop to iterate from 0 to 100 and print only even numbers

for j in range(0,102,2):
    print(j,' ', end='')
print(' ')
# Q8 Use for loop to iterate from 0 to 100 and print only odd numbers
for h in range(0,101,1):
    if h%2==0:
        pass
    else:
        print(h,' ',end='')
print(' ')

# Exercises: Level 2
# Q1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for j in range(0,102,2):
    sum=sum+j
print(sum)
# Exercises: Level 3
# Q1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
z=len(countries)
sum1=0
for k in range(0,z,1):
    if 'land'in countries[k]:
        sum1=sum1+1
        
        print(countries[k],' ',end='')
print(' ')
print('There is', sum1, 'countries that has land')

# Q2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
new_list=['banana', 'orange', 'mango', 'lemon']

xlen=len(new_list)
for d in range(-1,-n,-1):
    print(new_list[d], ' ', end='')
print('')

# Q3 Go to the data folder and use the countries_data.py file.