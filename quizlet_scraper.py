import requests
from bs4 import BeautifulSoup
from lxml import html

def replace_breaks(arr, t):
	string = ''
	if t == True:
		for each in arr:
			if isinstance(each, basestring):
				each = each.strip()
				string += '\t'+each
			else:
				string += '\n'
	else:
		for each in arr:
			if isinstance(each, basestring):
				string += each
			else:
				string += '\n'
	if string.isupper():
		string = '\n\n'+string
	return string

file = open('BI325_prototype.txt', 'w')

page = requests.get('https://quizlet.com/147776728/bi325-chapter-2-bi-325-chapter-3-bi325-chapter-4-bi325-chapter-5-bi325-chapter-6-bi325-chapter-7-bi325-chapter-8-bi325-chapter-9-flash-cards/?new')

soup = BeautifulSoup(str(page.content), 'lxml')

file.write(soup.title.string+'\n\n\n')

for each in soup.find_all('div', 'text'):
	spans = each.find_all('span')
	file.write(replace_breaks(spans[0].contents, False).encode('utf-8'))
	file.write('\n')
	file.write(replace_breaks(spans[1].contents, True).encode('utf-8'))
	file.write('\n\n')
	"""
	word = spans[0].contents[0]
	definition = spans[1].contents[0]
	raw = word + "," + definition+'\n'
	file.write(raw.encode('utf8'))
	"""