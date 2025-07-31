import keyword
from re import sub, IGNORECASE


def check_keyword(match_obj):
    s = match_obj.group(0)
    if s in keyword.kwlist or s.lower() in keyword.kwlist or s.capitalize() in keyword.kwlist:
        return '<kw>'
    else:
        return s

text = input()

newtext = sub(r'\b[a-zA-Z]{1,}\b', check_keyword, text, flags=IGNORECASE)

print(newtext)