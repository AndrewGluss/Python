from re import findall
import sys
from collections import defaultdict


data = [line.strip() for line in sys.stdin]

pattern1 = r'<(.{1,}?)>'
result = defaultdict(list)
for i in data:
    x = findall(pattern1, i)
    #print(x)
    for j in x:
        if j[0] != '/' and len(j.split()) > 1:
            #print(j)
            pattern2 = r'^([a-z\d]{1,})'
            y = findall(pattern2, j)
            #print(y)
            pattern3 = r'([a-z-]{1,})='
            z = findall(pattern3, j)
            #print(z)
            for k in y:
                if k not in result:
                    result[k] += z
                else:
                    for n in z:
                        if n not in result[k]:
                            result[k].append(n)

        elif j[0] != '/' and len(j.split()) == 1:
            #print(f'{j} вот так')
            if j not in result:
                result[j]

#print(result)

for key, value in dict(sorted(result.items())).items():
    print(f"{key}: {', '.join(sorted(value))}")