
# import urllib.request
# import urllib.parse
# import urllib.error
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pre4e.org/romeo.txt')
for lines in fhand:
    print(lines.decode())

    
