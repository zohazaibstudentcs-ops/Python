import urllib.request
import xml.etree.ElementTree as ET

# Ask the user for a URL; if they just press enter, use the default assigned data file
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2462866.xml'

print('Retrieving', url)

# Open the URL and read the raw XML data from it
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Parse the XML string into a tree object we can search through
tree = ET.fromstring(data)

# Find every <count> tag anywhere in the tree, no matter how deep it's nested
counts = tree.findall('.//count')

nums = list()
for result in counts:
    # Debug print the data :)
    print(result.text)          # show each count value as text, to check it's reading correctly
    nums.append(int(result.text))  # convert the text to a number and store it in the list

# Show how many count values were found, and their total
print('Count:', len(nums))
print('Sum:', sum(nums))