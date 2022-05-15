import pickle
import random

'''
Save_dict function opens binary file with dictionary containing savings names as keys
and the tuple containing the puzzled number and the number of attempts as values.
The function converts binary to text, adds the new key:value to the dictionary
and returns a binary file with new saving.

Note that the binary file should be created before running the function.

'''

def save_dict(dict_to_add, file):
    save_file = open(file, "rb") # open file for reading
    saved_dict = pickle.load(save_file) # convert binary to text
    save_file.close() # close file
    save_file = open(file, "wb") # open file for writing
    saved_dict.update(dict_to_add) # add new key:value to the existed dictionary
    pickle.dump(saved_dict, save_file) # convert text to binary
    save_file.close() # close file

# choice start a new game or load a saved game

choice = input("Please select an option:\n"
          "1. Start a new game.\n"
          "2. Load the game.\n")

# play the game from the beginning

if int(choice) == 1:
    # puzzle a random number and start attempt counting
    x = random.randint(0, 100)
    count = 0
    # run the game
    print(x)
    while count < 9:
        user_input = input("Enter integer: ")
        if user_input.isalpha() == True:
            if str(user_input) == "S" or str(user_input) == "s":
                name = input('Enter a saving name: ')
                new_dict = {name: (count - 1, x)}
                save_dict(new_dict, "D:\PYTHON_course\game_save\game_dump.pkl")
                print("Your game is saved. See you later!")
                break
            else:
                print("Incorrect input. Type integer to continue the game or type S/s for saving")
        else:
            if int(user_input) == x:
                print("Congratulations!")
                print("Counts = " + str(count))
                break
            else:
                print("Incorrect, try again.")
                count = count + 1
                continue
    else:
        user_input = input("This is the last try. Enter integer: ")
        if user_input.isalpha() == True:
            if str(user_input) == "S" or str(user_input) == "s":
                name = input('Enter a saving name: ')
                new_dict = {name: (count - 1, x)}
                save_dict(new_dict, "D:\PYTHON_course\game_save\game_dump.pkl")
                print("Your game is saved. See you later!")
        else:
            if int(user_input) == x:
                print("Congratulations!")
                print("Counts = " + str(count))
            else:
                print("Failure!")
                print("Counts = " + str(count + 1))

# continue a saved game

if int(choice) == 2:

    # load saved game

    open_file = open("D:\PYTHON_course\game_save\game_dump.pkl", "rb") #открываем файл
    savings_dict = pickle.load(open_file)
    print("The following savings are available:")
    print(*savings_dict.keys())
    selected_saving = str(input('Enter the saving name: '))
    count = savings_dict[selected_saving][0]
    x = savings_dict[selected_saving][1]
    print(x)
    print(count)

    # run the selected game

    while count < 9:
        user_input = input("Enter integer: ")
        if user_input.isalpha() == True:
            if str(user_input) == "S" or str(user_input) == "s":
                name = input('Enter a saving name: ')
                new_dict = {name: (count - 1 , x)}
                save_dict(new_dict, "D:\PYTHON_course\game_save\game_dump.pkl")
                print("Your game is saved. See you later!")
                break
            else:
                print("Incorrect input. Type integer to continue the game or type S/s for saving")
        else:
            if int(user_input) == x:
                print("Congratulations!")
                print("Counts = " + str(count))
                break
            else:
                print("Incorrect, try again.")
                count = count + 1
                continue
    else:
        user_input = input("This is the last try. Enter integer: ")
        if user_input.isalpha() == True:
            if str(user_input) == "S" or str(user_input) == "s":
                name = input('Enter a saving name: ')
                new_dict = {name: (count - 1, x)}
                save_dict(new_dict, "D:\PYTHON_course\game_save\game_dump.pkl")
                print("Your game is saved. See you later!")
        else:
            if int(user_input) == x:
                print("Congratulations!")
                print("Counts = " + str(count))
            else:
                print("Failure!")
                print("Counts = " + str(count + 1))

