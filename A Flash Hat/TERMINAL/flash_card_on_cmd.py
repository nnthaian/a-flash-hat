import csv
import random
import os
import time
from sys import platform

## WIN ver: open the cmd_WIN_run.bat to run the code smoothly and see clearly how the clrscr def is used
## to define functions in the program.

## MAC ver: open the cmd for better (run the terminal)

def readVocabCSV(filename):
    '''
    this function is to read the csv file already in the program.
    parameter:
        filename: the name of the csv file
    return:
        output_data: a list containing multiple tuples of the form (word, definition)
    '''
    with open(f'vocab/{filename}.csv', 'r', encoding='utf-8') as f:
        csv_data = csv.reader(f)
        output_data = []
        for i in csv_data:
            output_data.append(tuple(i))
        output_data = output_data[1:]
        return output_data


def clrscr():
    '''
    this function is to clear the running screen.
    '''
    if platform == 'win32':
        os.system('cls')
    elif platform == 'darwin':
        os.system('clean')
    else:
        print('Cannot clear screen. Clearing manually')
        print('\n' * 100)


def chooseVocabList():
    '''
    this function is to prompt the user to choose their flash card to review or take a test.
    return:
        vocab_list: a list of tuples (word, definition)
    '''
    user_input = input("""We have 4 flash cards:
    [1] B2 Vocabulary
    [2] Environment
    [3] Climate change
    [4] Most common english verbs in spanish
>>> """)
    try:
        user_input = int(user_input)
    except:
        print('Invalid input')
        return -1
    vocab_list = []
    if user_input == 1:
        vocab_list = readVocabCSV('B2_vocab')
    elif user_input == 2:
        vocab_list = readVocabCSV('environment_vocab')
    elif user_input == 3:
        vocab_list = readVocabCSV('Global-Climate-Change_vocabulary')
    elif user_input == 4:
        vocab_list = readVocabCSV('spanish_vocab')
    return vocab_list


def game_Review():
    '''
    this function is to show all the words in the flash card the user have chosen.
    return:
        0: Menu
        1: Review
        2: Test
    '''
    vocab_list = chooseVocabList()
    for i, word in enumerate(vocab_list):
        print(f'{i + 1}. {word[0]}: {word[1]}')
        time.sleep(1 / 10)
    print()
    user_input = input('''Flash cards reviewed!
    If you want to go back to the menu, enter 0.
    If you want to review another flash card, enter 1.
    If you want to take a test, enter 2.
>>> ''')
    try:
        user_input = int(user_input)
        if user_input == 1:
            return 1
        elif user_input == 2:
            return 2
        else:
            return 0
    except:
        print('Invalid input')
        return 0


def game_MultipleChoice():
    '''
    this function is to help the user learn the word in the selected flash card by using multiple choice.
    return:
        0: Menu
    '''
    vocab_list = chooseVocabList()
    testing_sample = random.sample(vocab_list, k=15)
    word_counter = [0] * 15
    for i in range(3):
        print(f'Starting round {i + 1}...')
        current_words = list(range(i * 5, i * 5 + 5))
        current_points = 0
        while current_points < 100:
            current_right_answer = random.choice(current_words)
            wrong_answer = random.sample(testing_sample, 4)
            lst_user_answer = [testing_sample[current_right_answer]]
            for j in wrong_answer:
                if j != testing_sample[current_right_answer]:
                    lst_user_answer.append(j)
                    if len(lst_user_answer) == 4:
                        break
            random.shuffle(lst_user_answer)
            print('-' * 120)
            user_answer = input(
                f"""What the meaning of {testing_sample[current_right_answer][0]}:
    A: {lst_user_answer[0][1]}
    B: {lst_user_answer[1][1]}
    C: {lst_user_answer[2][1]}
    D: {lst_user_answer[3][1]}
>>> """
            )
            user_answer = user_answer.lower()
            if user_answer == 'a':
                user_answer = lst_user_answer[0][0]
            if user_answer == 'b':
                user_answer = lst_user_answer[1][0]
            if user_answer == 'c':
                user_answer = lst_user_answer[2][0]
            if user_answer == 'd':
                user_answer = lst_user_answer[3][0]
            if user_answer == testing_sample[current_right_answer][0]:
                print('Correct')
                current_points += 5
                word_counter[current_right_answer] += 1
                if word_counter[current_right_answer] == 4:
                    current_words.remove(current_right_answer)
            else:
                print('Incorrect')
            print(f'You are currently at {current_points}/100 points')
        print(f'Round {i + 1} finished!')
        print('*')
    print('Congratulations!')
    input('Press Enter to go back')
    return 0


def game_ShortAnswer():
    '''
    this function is to help the user learn the word in the selected flash card by short answer.
    return:
        0: Menu
    '''
    vocab_list = chooseVocabList()
    testing_sample = random.sample(vocab_list, k=15)
    word_counter = [0] * 15
    for i in range(3):
        print(f'Starting round {i + 1}...')
        current_words = list(range(i * 5, i * 5 + 5))
        current_points = 0
        while current_points < 100:
            current_question = random.choice(current_words)
            print('-' * 120)
            user_answer = input(f'What is: "{testing_sample[current_question][1]}":\n>>> ')
            if user_answer == testing_sample[current_question][0]:
                print('Correct!')
                current_points += 5
                word_counter[current_question] += 1
                if word_counter[current_question] == 4:
                    current_words.remove(current_question)
            else:
                print('Incorrect!')
            print(f'You are currently at {current_points}/100 points')
        print(f'Round {i + 1} finished!')
        print('*')
    print('Congratulations!')
    input('Press Enter to go back')
    return 0


def game_Test():
    '''
    this function is to prompt the user to select the test or go back to the menu.
    return:
         game_ShortAnswer(): go to short answer function and run it
         game_MultipleChoice(): go to multiple choice function and run it
         0: go back to Menu
    '''
    user_input = input("""There are two ways to learn:
    [1] Short Answer
    [2] Multiple Choice
    [0] Back to Menu
>>> """)
    try:
        user_input = int(user_input)
    except:
        print('Invalid input')
        return -1
    if user_input == 1:
        return game_ShortAnswer()
    elif user_input == 2:
        return game_MultipleChoice()
    else:
        return 0


def game_Introduction():
    '''
    this function is to print the introduction about A FLASH HAT and how the
    return:
        0: Menu
    '''
    print("""
    Welcome to A Flash Hat! Before jumping into learning and practicing your first vocabulary set, let us walk
    you through some of our main available functions.
    At Review, all words are displayed for you to revise before letting your memory be tested.
    After that, there are two types of memory testing games in Test, which are Multiple Choice and Short Answer.
    
    Rules for Test:
    There are lists of words for 3 rounds, each round having 5 words. The user is recommended to learn all 15 words. 
    If correct, bonus 5 points. A word is set to Passed if the user reaches 20 points. The session ends when the
    user finishes memorizing all 15 words. Memorizing test can stop when the user answers all the cards correctly.

    """)
    input('Press Enter to go back')
    return 0


def chooseMode():
    '''
    this funtion is to prompt the user to select option from the menu.
    return:
        user_input: save the user_input to run the selected function in main()
        -1: Exit
    '''
    print('Welcome to A FLASH HAT.')
    print('Menu:')
    print('[1] Review')
    print('[2] Test')
    print('[3] Introduction about A FLASH HAT')
    print('[-1] Exit the program')
    user_input = input('Select: ')
    try:
        user_input = int(user_input)
        return user_input
    except:
        print('Invalid input')
        return -1


def main():
    '''
    this function is to control the flow of the program.
    '''
    clrscr()
    chosen_mode = chooseMode()
    while chosen_mode != -1:
        clrscr()
        if chosen_mode == 0:
            chosen_mode = chooseMode()
        elif chosen_mode == 1:
            chosen_mode = game_Review()
        elif chosen_mode == 2:
            chosen_mode = game_Test()
        elif chosen_mode == 3:
            chosen_mode = game_Introduction()
        else:
            break


if __name__ == '__main__':
    main()

"""
    Feature Code:
        -1 - Exit
        0 - Menu
        1 - Review
        2 - Test
        3 - Introduction
"""
