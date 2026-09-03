import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse JSON data
info = json.loads(data)

# Access the 'comments' array and extract counts
comments = info['comments']
print('Count:', len(comments))

# Calculate the sum of all count values
total_sum = sum(item['count'] for item in comments)
print('Sum:', total_sum)