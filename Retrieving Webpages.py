import urllib.request

# Open the URL like a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Iterate line by line
for line in fhand:
    # Decode bytes to Unicode string and strip whitespace
    clean_line = line.decode().strip()
    print(clean_line)