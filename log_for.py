def log_for(filename, date):
    with open(filename, 'r', encoding='utf-8') as file1, open(f'log_for_{date}.txt', 'w', encoding='utf-8') as file2:
        data = file1.readlines()
        for line in data:
            words = line.split()
            if words[0] == date:
                file2.write(" ".join(words[1:]) + "\n")


with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())