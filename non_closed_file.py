def non_closed_files(files):
    return [file for file in files if file.closed == False]

with (
    open('file1.txt', 'w', encoding='utf-8') as file1,
    open('file2.txt', 'w', encoding='utf-8') as file2,
    open('file3.txt', 'w', encoding='utf-8') as file3
):
    file1.write('i am the first file')
    file2.write('i am the second file')
    file3.write('i am the third file')

file1 = open('file1.txt', encoding='utf-8')
file3 = open('file3.txt', encoding='utf-8')


for file in non_closed_files([file1, file2, file3]):
    print(file.read())