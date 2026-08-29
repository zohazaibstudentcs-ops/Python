import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)

# Print the final URL retrieved (the 7th hop)
print('Retrieving:', url)

# Extract and print just the name from the final URL
name = url.split('_')[-1].split('.')[0]
print('Last name in sequence:', name)