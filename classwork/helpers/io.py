'''
The logger function adds an input text to the end of the input file.

'''

def logger(message, file_path):  # save text to file function
    error_log = open(file_path, "at")  # open file for writing to the end of file
    error_log.write(message + "\n") # save input message to the opened file
    error_log.close
