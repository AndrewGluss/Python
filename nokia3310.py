d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
message = input()
nokia3310 = ''
for i in message:
    for key, value in d.items():
        if i.upper() in value:
            stroka = value
            x = (stroka.index(i.upper())) + 1
            c = 0
            while c < x:
                nokia3310 += key
                c += 1
print(nokia3310)