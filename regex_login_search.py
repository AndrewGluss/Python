import sys
from re import search

pattern_login = r'_\d{1,}[a-zA-Z]{0,}(_){,1}$'

data = [line.strip() for line in sys.stdin]

for i in data:
    match_login = search(pattern_login, i)
    if match_login:
        print(True)
    else:
        print(False)