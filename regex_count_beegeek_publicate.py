import sys
from re import search, IGNORECASE

pattern = r'.{0,}beegeek.{0,}'

data = [line.strip() for line in sys.stdin]
count = 0

for i in data:
    x = search(pattern, i, flags=IGNORECASE)

    if x:
        count += 1

print(count)