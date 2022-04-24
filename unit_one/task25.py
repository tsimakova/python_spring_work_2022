#todo: Убрать повторяющиеся буквы и лишние символы

'''
Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

Input             	            Output
apple	                        aple
25.04.2022 Good morning !!	    godmrni

'''


'''
The keep_unique_letters function remove all characters from the string except letters.
For all duplicated letters only first instance is preserved. 

'''

def keep_unique_letters(text):
    temp_list = []
    for i in text:
        if i.isdigit() == True:
            continue
        if i.isalpha() == False:
            continue
        else:
            temp_list.append(i.lower())

    return(list(dict.fromkeys(temp_list)))


inp1 = 'apple'
out1 = keep_unique_letters(inp1)
print(out1)

inp2 = '25.04.2022 Good morning !!'
out2 = keep_unique_letters(inp2)
print(out2)







