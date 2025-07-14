from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zf:
    #zf.printdir()
    info = zf.infolist()
    count = 0
    for i in info:
        if i.is_dir() == False:
            count += 1
    print(count)