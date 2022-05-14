import pickle

def save_dict(dict, file):
    save_file = open(file, "rb") # open file for reading
    saved_dict = pickle.load(save_file) # convert binary to text
    save_file.close() # close file
    save_file = open(file, "wb") # open file for writing
    saved_dict.update(dict) # add new key:value to the existed dictionary
    pickle.dump(saved_dict, save_file) # convert text to binary
    save_file.close() # close file


save_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "wb")
saved_dict = {}
pickle.dump(saved_dict, save_file)
save_file.close()

tup1 = {'test1': (3, 8), 'test2': (5, 12)}
tup2 = {'test3': (7, 9)}

save_dict(tup1, "D:\PYTHON_course\game_save\game_dump.pkl")
save_dict(tup2, "D:\PYTHON_course\game_save\game_dump.pkl")

open_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "rb") #открываем файл
saved_dict = pickle.load(open_file)
print(saved_dict)
save_file.close()


'''
saved_dict = {}


save_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "wb")
saved_dict.update(tup1)
pickle.dump(saved_dict, save_file)
save_file.close()

open_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "rb")
saved_dict = pickle.load(open_file)
save_file.close()
save_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "wb")
saved_dict.update(tup2)
pickle.dump(saved_dict, save_file)
save_file.close()


open_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "rb") #открываем файл
saved_dict = pickle.load(open_file)
print(saved_dict)
save_file.close()


'''
