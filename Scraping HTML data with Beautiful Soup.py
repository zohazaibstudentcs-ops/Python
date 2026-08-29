import urllib.request
from bs4 import BeautifulSoup
# Prompt for the URL
url = input('Enter - ')
# Read the HTML content from the URL
html = urllib.request.urlopen(url).read()
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
# Find all <span> tags in the document
tags = soup('span')
# Initialize counters for the numbers and their sum
count = 0
total_sum = 0
# Loop through all <span> tags
for tag in tags:
    # Get the text contents inside the <span> tag and convert it to an integer
    number = int(tag.contents[0])
    
    # Update count and sum
    count += 1
    total_sum += number
# Print the results
print('Count', count)
print('Sum', total_sum)