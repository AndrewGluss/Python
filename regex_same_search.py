import sys
from re import search

pattern = r'\b(.{1,})\1\b'

data = [line.strip() for line in sys.stdin]

for i in data:
    match_login = search(pattern, i)
    if match_login:
        print(match_login.group())