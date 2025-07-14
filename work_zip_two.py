from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zf:
    #zf.printdir()
    info = zf.infolist()
    before_volume = 0
    after_volume = 0
    for i in info:
        before_volume += i.file_size
        after_volume += i.compress_size

    print(f"Объем исходных файлов: {before_volume} байт(а)")
    print(f"Объем сжатых файлов: {after_volume} байт(а)")