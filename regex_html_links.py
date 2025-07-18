from re import findall
import sys

data = [line.strip() for line in sys.stdin]

pattern = r"<a href=\"(.{1,}?)\">(.{1,})</a>"

for i in data:
    x = findall(pattern, i)

    for i in x:
        print(f"{i[0]}, {i[1]}")