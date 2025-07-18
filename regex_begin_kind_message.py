from re import search, match, IGNORECASE

msg = input()
pattern1 = r'^(Здравствуйте)' # [(Здравствуйте)(Доброе утро)(Добрый день)(Добрый вечер)]
pattern2 = r'^(Доброе утро)'
pattern3 = r'^(Добрый день)'
pattern4 = r'^(Добрый вечер)'

pattern = r"^Здравствуйте|^Доброе утро|^Добрый (день|вечер).*"

match1 = match(pattern1, msg, flags=IGNORECASE)
match2 = match(pattern2, msg, flags=IGNORECASE)
match3 = match(pattern3, msg, flags=IGNORECASE)
match4 = match(pattern4, msg, flags=IGNORECASE)

if match1 or match2 or match3 or match4:
    print(True)
else:
    print(False)