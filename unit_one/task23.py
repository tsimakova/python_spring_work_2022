#todo: Взлом шифра
'''
Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.

grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

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

eng_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = 'grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua\'xk jazin.'

fd = open('D:\out.txt', 'w', encoding = 'utf-8')

temp_list = []
coded_text = ''

for i in range(len(eng_alfa)):
    new_dict = shift_left(eng_alfa, i)
    newlines = code_text(eng_alfa, new_dict, message)
    i = i + 1
    coded_text += (newlines + '\n')
    temp_list.append(coded_text)

fd.write(temp_list[-1])
fd.close

#  Answer: although that way may not be obvious at first unless you're dutch.
#  Encripting method: left-shift for 7 letteres.
