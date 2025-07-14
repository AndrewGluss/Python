from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', 'r') as zf:
    #zf.printdir()
    info = zf.infolist()
    list_filenames = []
    for i in info:
        if i.is_dir() == False:
            #list_filenames.append(i.filename.split('/')[-1])
            list_filenames.append(tuple([i.filename.split('/')[-1], datetime.strptime(f'{i.date_time[0]}-{i.date_time[1]}-{i.date_time[2]} {i.date_time[3]}:{i.date_time[4]}:{i.date_time[5]}', '%Y-%m-%d %H:%M:%S'), i.file_size, i.compress_size]))
    sort_list = sorted(list_filenames, key=lambda x: x[0])
    for file in sort_list:
        print(file[0])
        print(f'  Дата модификации файла: {datetime.strftime(file[1], "%Y-%m-%d %H:%M:%S")}')
        print(f'  Объем исходного файла: {file[2]} байт(а)')
        print(f'  Объем сжатого файла: {file[3]} байт(а)\n')
