import pygame, sys
import classes_of_main as classes
from pygame import mixer

import csv
lstDefinitions = []
lstDecks = []
lstDecksWords = []
lstWords = []

#available deck
with open('vocab/B2_vocab.csv', mode='r') as file:
    content = csv.reader(file)
    myDeck = {row[0]:row[1] for row in content}
    lstWords = list(myDeck.keys())
lstDecks.append(myDeck)
lstDecksWords.append(lstWords)

lstWords = []
with open('vocab/Global-Climate-Change_vocabulary.csv', mode='r') as file:
    content = csv.reader(file)
    myDeck = {row[0]:row[1] for row in content}
    lstWords = list(myDeck.keys())
lstDecks.append(myDeck)
lstDecksWords.append(lstWords)

lstWords = []
with open('vocab/environment_vocab.csv', mode='r') as file:
    content = csv.reader(file)
    myDeck = {row[0]:row[1] for row in content}
    lstWords = list(myDeck.keys())
lstDecks.append(myDeck)
lstDecksWords.append(lstWords)


lstWords = []
with open('vocab/spanish_vocab.csv', mode='r') as file:
    content = csv.reader(file)
    myDeck = {row[0]:row[1] for row in content}
    lstWords = list(myDeck.keys())
lstDecks.append(myDeck)
lstDecksWords.append(lstWords)

#basic
pygame.init()
clock = pygame.time.Clock()

#set up
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('image/A Flash Hat')
icon = pygame.image.load('image/logo.png')
pygame.display.set_icon(icon)

#button using more than 1 time
back_button = classes.Button(10, 10, pygame.image.load('image/back_button.png'))
home_button = classes.Button(620, 200,pygame.image.load('image/home_button.png'))
continue_button = classes.Button(620, 410, pygame.image.load('image/continue_button.png'))

#background:
BG_writing = pygame.image.load('image/BG sa.png')
BG_mpchoice = pygame.image.load('image/BG mp.png')
BG_end = pygame.image.load('image/BG end test.png')

BG_menu = pygame.image.load('image/BG menu.png')
BG_test = pygame.image.load('image/BG test.png')
BG_review = pygame.transform.scale((pygame.image.load('image/BG Review.png')), (SCREEN_WIDTH,SCREEN_HEIGHT))
BG_select_deck = pygame.transform.scale((pygame.image.load('image/BG select deck.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))
ready_sa = pygame.image.load('image/ready_sa.png')
ready_mp = pygame.image.load('image/ready_mp.png')

intro = pygame.image.load('image/intro.png')
rules = pygame.image.load('image/rules.png')
announcement = pygame.image.load('image/announcement.png')

#background music
mixer.music.load('other/background_music.mp3')
##continue playing until we close the program
mixer.music.play(-1)

DECK_SIZE = (500, 300)
buttonDeck1 = classes.Button(25,200, pygame.transform.scale(pygame.image.load('image/Button_Deck1_B2Vocab.png'), DECK_SIZE))
buttonDeck2 = classes.Button(520,200, pygame.transform.scale(pygame.image.load('image/Button_Deck2_ClimateChange.png'), DECK_SIZE))
buttonDeck3 = classes.Button(25,425, pygame.transform.scale(pygame.image.load('image/Button_Deck3_Environment.png'), DECK_SIZE))
buttonDeck4 = classes.Button(520,425, pygame.transform.scale(pygame.image.load('image/Button_Deck4_Spanish.png'), DECK_SIZE))


def menu():
    '''
    this function is to create a menu with 3 buttons: Test, Info and Review .
    '''
    running = True
    review_button = classes.Button(400, 340, pygame.image.load('image/review_button.png'))
    test_button = classes.Button(400, 430, pygame.image.load('image/test_button.png'))
    info_button = classes.Button(400, 520, pygame.image.load('image/info_button.png'))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        screen.blit(BG_menu, (0,0))
        if test_button.update_n_check_click(screen):
            test_function()
        if review_button.update_n_check_click(screen):
            select_deck_function()
        if info_button.update_n_check_click(screen):
            info_function()
        pygame.display.update()
        clock.tick(60)

def select_deck_function():
    '''
    the function is to select the deck.
    '''
    while True:
        screen.blit(BG_select_deck, (0,0))
        buttonDeck1.show(screen)
        buttonDeck2.show(screen)
        buttonDeck3.show(screen)
        buttonDeck4.show(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if buttonDeck1.update_n_check_click(screen):
                review_function(0)
            if buttonDeck2.update_n_check_click(screen):
                review_function(1)
            if buttonDeck3.update_n_check_click(screen):
                review_function(2)
            if buttonDeck4.update_n_check_click(screen):
                review_function(3)

        if back_button.update_n_check_click(screen):
            menu()

        back_button.draw(screen)
        pygame.display.update()
        clock.tick(60)


def info_function():
    '''
    this function is to create an introduction about A Flash Hat and test rules.
    '''
    change_screen = 0
    while True:
        screen.blit(intro, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and change_screen <= 2:
                    change_screen += 1
        if change_screen == 1:
            screen.blit(rules, (0,0))
        if change_screen == 2:
            screen.blit(announcement, (0,0))
        if change_screen == 3:
            menu()
        pygame.display.update()
        clock.tick(60)

def test_function():
    '''
    this function is to create an interface with 2 buttons: Writing and Multiple Choice
    '''
    mp_button = classes.Button(528, 180, pygame.image.load('image/mp_select.png'))
    writing_button = classes.Button(138, 180, pygame.image.load('image/sa_select.png'))
    while True:
        screen.blit(BG_test, (0,0))
        back_button.draw(screen)
        mp_button.draw(screen)
        writing_button.draw(screen)
        if back_button.check_click_only(screen):
            menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mp_button.check_click_only(screen):
                    multiple_choice_function()
                if writing_button.check_click_only(screen):
                    writing_function()

        pygame.display.flip()
        clock.tick(60)

def review_function(deckID):
    '''
    the function is to create a interface to see the words in the dictionary.
    :param deckID: ID of the deck
    '''
    lstWords = lstDecksWords[deckID]
    myDeck = lstDecks[deckID]
    lstCards = []
    for word in lstWords:
        new_card = classes.Card(word, myDeck[word])
        lstCards.append(new_card)

    lstPages = []
    lstCardsEachPage = list(classes.Page.createCardsEachPage(lstCards, classes.Page.MAX_PER_PAGE))
    for index, item in enumerate(lstCardsEachPage):
        new_page = classes.Page(index, item)
        lstPages.append(new_page)
    page_number = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and page_number < len(lstPages)-1:
                    page_number+=1
                if event.key == pygame.K_LEFT and page_number > 0:
                    page_number-=1
        if back_button.update_n_check_click(screen):
            menu()

        screen.blit(BG_review, (0,0))
        back_button.draw(screen)
        lstPages[page_number].draw(screen)
        lstPages[page_number].numeratePage(len(lstPages), screen)
        pygame.display.update()
        clock.tick(60)

def multiple_choice_function():
    '''
    this function is to create an interface of multiple choice test.
    '''
    change_screen = 0
    while True:
        screen.blit(ready_mp, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and change_screen <= 1:
                    change_screen += 1
        if change_screen == 1:
            screen.blit(BG_mpchoice, (0,0))
        if change_screen == 2:
            screen.blit(BG_end, (0,0))
            if home_button.update_n_check_click(screen):
                menu()
            if continue_button.update_n_check_click(screen):
                multiple_choice_function()
        pygame.display.update()
        clock.tick(60)

def writing_function():
    '''
    this function is to create an interface of short answer test.
    '''
    change_screen = 0
    while True:
        screen.blit(ready_sa, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and change_screen <= 1:
                    change_screen += 1
        if change_screen == 1:
            screen.blit(BG_writing, (0,0))
        if change_screen == 2:
            screen.blit(BG_end, (0,0))
            if home_button.update_n_check_click(screen):
                menu()
            if continue_button.update_n_check_click(screen):
                writing_function()
        pygame.display.update()
        clock.tick(60)

# # #build the main function
if __name__ == "__main__" :
    menu()
