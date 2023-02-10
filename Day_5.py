first_list=[]
print(first_list)
secound_list=['tanimu',3,'abdullahi','BUK',4.7,'hen']
print(len(secound_list))
mixed_data_types=['tanimu',36,12.4,'married','hausawa sabon titi, model primary school']
print(mixed_data_types)
companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(companies)
print(len(companies))
y=int(len(companies)/2)
print(y)
print('the first',companies[0])
print('the mid is',companies[y])
print('the last is',companies[-1])
companies[1]='Netflix'
print(companies)
companies.append('IT Comapany')
companies.insert(y,'IT Comapany')
print(companies)
x=companies[0]

print(x.upper())

str_1=['#']
str_2=companies+str_1
print(str_2)

does_exit='Apple' in companies
print(does_exit)

companies.sort()
print(companies)

companies.reverse()
print(companies)

print(companies[3:])

print(companies[:-3])

n=int(len(companies)/2)
print(companies[n:])
y=companies.pop(0)
print(y)
print(companies)

n=int(len(companies)/2)
print(companies.pop(n))

print(companies.pop(-1))

companies.clear()
print(companies)

del companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back_comb=front_end+back_end
full_stack=front_back_comb.copy()
print(full_stack)
x=full_stack.index('Redux')
print(x)
full_stack.insert(x+1,'python')
full_stack.insert(x+2,'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
x=min(ages)
y=max(ages)
print(x,y)

x_length=len(ages)
ages.insert(x_length,x)
ages.insert(x_length+1,y)
print(ages)
md=int(len(ages)/2)
if len(ages)%2==0:
    medium_even=int((ages[md-1]+ages[md])/2)
    print()
    print('the medium of two numbers is', medium_even)
else:
    medium_odd=ages[md]
    print('the medium of odd is', medium_odd)

sum_list=sum(ages)
average_list=sum_list/len(ages)
print('the average is', average_list)

x_ranges=y-x  #y= max. x=min
print('the ranges is', x_ranges)

x_compare= abs(x-average_list)
print(x_compare)
y_comapre=(y-average_list)
print(y_comapre>x_compare)

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
countries_len=len(countries)
countries_medium=int(countries_len/2)
print('the countries medium is', countries[countries_medium])

if countries_len%2==0:
    print(" ")
else:  
    countries.insert(int(countries_len/2),'Nigeria') 
    print(countries)

XYZ=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
x,y,z,*r=XYZ
print(x,y,z)
print(r)