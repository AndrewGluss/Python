import sys
from re import search

pattern_phone = r'(?P<contry>\d{1,3})([- ])(?P<city>\d{1,3})([- ])(?P<phone>\d{4,10})'

data = [line.strip() for line in sys.stdin]

for i in data:
    march_phone = search(pattern_phone, i)
    print(f'Код страны: {march_phone.groupdict()["contry"]}, Код города:  {march_phone.groupdict()["city"]}, Номер:  {march_phone.groupdict()["phone"]}')
