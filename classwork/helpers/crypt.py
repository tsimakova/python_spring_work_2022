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
