import sys

class UpperPrint:

    def __enter__(self, *args, **kwargs):
        self.standard_output = sys.stdout.write
        sys.stdout.write = lambda text: self.standard_output(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.standard_output


print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')