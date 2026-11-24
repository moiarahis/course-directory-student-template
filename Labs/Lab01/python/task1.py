latin_alphabet = "abcdefghijklmnopqrstuvwxyz"
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text_latin = "venividivici"             #входной текст
shift = 3                               #длина  сдвига
encrypted_latin = ""                    #переменная для зашифрованного текста

#алгоритм шифрования
for char in text_latin:
    if char in latin_alphabet:
        idx = latin_alphabet.index(char)
        new_idx = (idx + shift) % len(latin_alphabet)
        encrypted_latin += latin_alphabet[new_idx]
    else:
        encrypted_latin += char

descrypted_latin = ""                   #переменная для расшифрованного текста
for char in encrypted_latin:            #алгоритм дешифровки текста
    if char in latin_alphabet:
        idx = latin_alphabet.index(char)
        new_idx = (idx - shift) % len(latin_alphabet)
        descrypted_latin += latin_alphabet[new_idx]
    else:
        descrypted_latin += char

#вывод результатов алгоритма
print (f"Исходный:      {text_latin}")          #вывод исходного текста
print (f"Зашифрованный:      {encrypted_latin}")          #вывод зашифрованного текста
print (f"Расшифровка:      {descrypted_latin}")          #вывод расшифрованного текста
print ()

