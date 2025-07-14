from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zf:
    #zf.printdir()
    info = zf.infolist()
    before_volume = 0
    after_volume = 0
    name_f = ""
    koeff = 100
    for i in info:
        if i.is_dir() == False:
            # before_volume += i.file_size
            # after_volume += i.compress_size
            #print(i.filename, i.file_size, i.compress_size)
            if (i.compress_size / i.file_size) * 100 < koeff:
                koeff = (i.compress_size / i.file_size) * 100
                name_f = i.filename

    #print(f"Объем исходных файлов: {before_volume} байт(а)")
    #print(f"Объем сжатых файлов: {after_volume} байт(а)")

    print(name_f.split('/')[-1])