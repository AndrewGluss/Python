from zipfile import ZipFile

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('desktop.zip', 'r') as zf:
    info = zf.infolist()
    for i in info:
        name_dir = ''
        if i.is_dir():
            name_dir = [i for i in i.filename.split('/') if len(i) > 0][-1]
            tabs = '  '*(len([i for i in i.filename.split('/') if len(i) > 0])-1)
            print(f'{tabs}{name_dir}')
        else:
            name_file = [i for i in i.filename.split('/') if len(i) > 0][-1]
            tabs = '  '*(len([i for i in i.filename.split('/') if len(i) > 0])-1)
            print(f'{tabs}{name_file} {convert_bytes(i.file_size)}')