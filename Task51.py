# Задача1.
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"". 

import os
os.system('cls')

text = 'привет абвтный товарищ и спабвисибо забв благодарю за помощь'

def repl_word(text: str):
    if 'абв' not in text.lower():
        text = text.replace(text, ' ')
        return text
text = list(filter(repl_word, text.split()))
print(' '.join(text))
