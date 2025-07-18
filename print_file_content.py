def print_file_content(file_path):
    try:
        file = open(file_path, 'r')
        data = file.read()
        print(data)
        file.close()
    except FileNotFoundError:
        print("Файл не найден")


with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.write('Сражения и путешествия берут своё')

print_file_content('Precepts_of_Zote.txt')