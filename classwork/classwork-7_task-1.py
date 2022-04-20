#todo: Написать функцию logger() которая принимает в качестве аргумента текст который дописывается
# в файл error.log Новое сообщение должно распологаться на новой строчки.

#import os

def logger(message, file_path)  # save text to file function
    error_log = open(file_path, "at")  # open file for writing to the end of file
    error_log.write(message + "\n") # save input message to the opened file
    error_log.close


mes = "This is an error message_3"
path = "D:\\PYTHON_course\\error.log"

logger(mes, path)
logger(mes, path)
