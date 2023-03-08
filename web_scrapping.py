# Q1 Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content 
soup = BeautifulSoup(content, 'html.parser') 
print(soup.title) 
print(soup.title.get_text()) 
print(response.status_code)
print(soup.get_text())
import json
y = json.dumps(soup.get_text())
print(y)



# Q2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3','cellpadding':'5'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)

    w=json.dumps(soup.td.text)
    print(w)



url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
#print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table')

# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
