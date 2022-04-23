# todo: Шифр Цезаря
'''

Описание шифра.
В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
является одним из самых простых и широко известных методов шифрования.
Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

Задача.
Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
В каждой строчке содержатся различные символы. Шифровать нужно только буквы латинского алфавита.

'''



'''
The shift_left function takes a list of letters (i.e. alphabet) as input
and creates the the dictionary with letters (keys) and thier IDs (values) in new alphabet
where all letters are round-shifted to the n letters to the left direction.   

'''

def shift_left(alphabet, n):
        key_dict = {}
        for j in alphabet:
                if (alphabet.index(j) - n) >= 0:
                    key_dict.update({j: (alphabet.index(j) - n)})
                if (alphabet.index(j) - n) < 0:
                    key_dict.update({j: ((alphabet.index(j) - n) + len(alphabet))})
                else:
                    continue
        return(key_dict)

'''
The code_text function takes alphabet, dictionary
with letters (keys) and thier IDs (values) in new alphabet generated
according to some rule, and the text
that should be coded accoring to the provided dictionary.

'''

def code_text(alphabet, key_dict, text):
    new_alf_id = []

    for i in range(len(text)):
        if text[i] in alphabet:
                new_alf_id.append(key_dict.get(text[i]))
        else:
            new_alf_id.append(str(text[i]))

    coded_text = ''

    for k in new_alf_id:
        if type(k) is int:
            coded_text += (alphabet[k])
        else:
            coded_text += str(k)
    return(coded_text)




alfa = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

fd = open("D:\message.txt", "r", encoding = "utf-8")

text = fd.readlines()

coded_text = ''
i = 1
for line in text:
    new_dict = shift_left(alfa, i)
    newlines = code_text(alfa, new_dict, line.lower())
    i = i + 1
    coded_text += newlines

print(coded_text)















