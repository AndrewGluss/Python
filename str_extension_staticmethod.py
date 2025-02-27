class StrExtension:
    @staticmethod
    def remove_vowels(text):
        vowels = 'aeoiuy'
        for i in text:
            if i.lower() in vowels:
                text = text.replace(i, '')
        return text

    @staticmethod
    def leave_alpha(text):
        for i in text:
            if i.isalpha() == False:
                text = text.replace(i, '')
        return text

    @staticmethod
    def replace_all(text, chars, new_char):
        for i in text:
            if i in chars:
                text = text.replace(i, new_char)
        return text

print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))


print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))