import re

reg = 'gmail'
text = 'Python Programming. for Absolute. Beginner'

s = 'abc 12-1234 12-02-2017, asd 56-1235 1-05-2016, xyz 78-1235 25-1-2018'

# match = re.findall('[^for]', text, re.I)

r = re.findall(r'\d{1,2}-\d\d?-\d{4}', s)
r = re.findall(r'\d{1,2}-\d\d?-(\d{4})', s)
r = re.findall(r'\d{1,2}-\d\d?-(\d{4})', s)
print(r)
