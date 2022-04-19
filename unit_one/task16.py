#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.

import random

print("Guess the word game!" + "\n"
      "You have 10 tries to guess the word by letters!" + "\n"
      "Each letter is present one time in a word." + "\n"
      "Hint! Use only lower case letters." + "\n")

def select_question(questions_list):  # random selection of a question from list of questions
    global question_number
    question_number = random.randint(0, len(questions_list) - 1)
    return questions_list[question_number]

def create_mask(answer_list):  # creation of a list of letters of the answer and the answer mask
    global word
    global mask
    word = [letter for letter in str(answer_list[int(question_number)])]
    mask = [symbol for symbol in str("_" * len(answer_list[int(question_number)]))]
    return mask

def play_game(answer_list):  # asking user and analyzing answers
    failure = 0  # failure counter
    success = 0  # success counter
    letter = str(input("Enter a letter "))  # first user try
    try_num = 10  # number of failures before game over
    while success < len(answer_list[int(question_number)]):  # run if guessed letters less than the word lenght
        if letter in word:  # run if guessed
            mask[int(word.index(letter))] = letter
            print(mask)
            success = success + 1
            if success == len(answer_list[int(question_number)]):  # run if whole word is guessed
                win = "Congratulations, you are win!"
                return win
            else:  # run if part of the word is guessed
                letter = str(input("Good, enter the next letter "))
                continue
        else:  # run if NOT guessed
            failure = failure + 1
            if failure < try_num:  # run if tries number is NOT exceeded
                letter = str(input("Oops, try again "))
                continue
            else:  # run if tries number is exceeded
                loose = "Sorry, game over!"
                return loose
                break

questions = ["Hereditary material in humans?", "Guido van Rossum's programming language?", "A version control system?"]
answers = ["dna", "python", "git"]


task = select_question(questions)
print(task)

task_mask = create_mask(answers)
print(task_mask)

game = play_game(answers)

