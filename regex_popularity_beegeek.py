import sys
from re import search, match, fullmatch

pattern1 = r'^(beegeek).{0,}(beegeek)$' # в 3 балла, если она начинается и заканчивается строкой beegeek
pattern2 = r'^(beegeek).*' # в 2 балла, если она только начинается или только заканчивается строкой beegeek
pattern3 = r'^[^(beegeek)]'
pattern5 = r'[^(beegeek)]$'
pattern6 = r'.*(beegeek)$'
pattern7 = r'.*beegeek.*'
pattern4 = 'beegeek'

famous = 0

data = [line.rstrip() for line in sys.stdin]

for i in data:
    match1 = fullmatch(pattern1, i)
    match2 = search(pattern2, i)
    match3 = search(pattern3, i)
    match4 = fullmatch(pattern4, i)
    match5 = search(pattern5, i)
    match6 = search(pattern6, i)
    match7 = search(pattern7, i)

    if match1:
        famous += 3
        #print(i)

    elif match4:
        famous += 2
        #print(i)

    # elif match2:
    #     if match6:
    #         famous += 2

    elif match2:
        if match5:
            famous += 2

    elif match6:
        if match3:
            famous += 2

    elif match7:
        famous += 1

print(famous)
