import requests
from bs4 import BeautifulSoup

result = requests.get("https://bulletin.andrews.edu/content.php?catoid=18&navoid=3948")
src = result.content
soup = BeautifulSoup(src, 'html.parser')


namesOfPrograms = []
for ul_tag in soup.find_all('ul', class_ = 'program-list'):
    for li_tag in ul_tag.find_all('li'):
        a_tag = li_tag.find('a')
        namesOfPrograms.append(a_tag.string)

print(namesOfPrograms)