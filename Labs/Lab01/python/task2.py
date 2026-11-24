latin_alphabet = "abcdefghijklmnopqrstuvwxyz"
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text_latin = "venividivici"             #входной текст
encrypted_latin = ""                    #переменная для зашифрованного текста

#отзеркеаливание букв алфавита
mapping_latin = {latin_alphabet[i]: latin_alphabet[len(latin_alphabet) - 1 - i] for i in range(len(latin_alphabet))}

for char in text_latin:
    if char in mapping_latin:
        encrypted_latin += mapping_latin[char]
    else:
        encrypted_latin += char

descripted_latin = ""                       #переменная для расшифрованного текста
for char in encrypted_latin:                #алгоритм дешифровки текста
    if char in mapping_latin:
        descripted_latin += mapping_latin[char]
    else:
        descripted_latin += char

#вывод результатов работы алгоритма
print ("Атбаш")
print (f"Исходный:          {text_latin}")
print (f"Зашифрованный:     {encrypted_latin}")
print (f"Расшифровка:       {descripted_latin}")
