import sys
from re import search

pattern1 = r'(bee)[ \w]{0,}\1{1,}'
pattern2 = r'\bgeek\b'
count_bee = 0
count_geek = 0

data = [line.strip() for line in sys.stdin]

for i in data:
    match1 = search(pattern1, i)
    match2 = search(pattern2, i)
    if match1:
        count_bee += 1
    if match2:
        count_geek += 1

print(count_bee)
print(count_geek)