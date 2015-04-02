import re

print(re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email).group())
