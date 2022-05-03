

from helpers.io import logger
from helpers.crypt import shift_left
from helpers.crypt import code_text


mes = "This is a helpers module test"
path = "D:\error.log"
logger(mes, path)


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
