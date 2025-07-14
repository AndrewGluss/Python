from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

# файлы из спискак названий файлов должны находиться в папке с файлом программы для успешного выполнения программы
with ZipFile('files.zip', 'w') as zip_file:
    for i in file_names:
        zip_file.write(i)