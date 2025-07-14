from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', 'r') as zf:
    #zf.printdir()
    info = zf.infolist()
    list_filenames = []
    point = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    for i in info:
        if i.is_dir() == False:
            if datetime.strptime(f'{i.date_time[0]}-{i.date_time[1]}-{i.date_time[2]} {i.date_time[3]}:{i.date_time[4]}:{i.date_time[5]}', '%Y-%m-%d %H:%M:%S') >= point:
                list_filenames.append(i.filename.split('/')[-1])

    print(*sorted(list_filenames), sep='\n')