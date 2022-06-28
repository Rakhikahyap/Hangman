import string
from word import choose_word
from image import IMAGES
def is_word_guessed(secret_word,a):
    if secret_word==get_guessed_word(secret_word,a):
        return True
    return False
def get_available_letters(a):
    # import string
    letters_left = string.ascii_lowercase
    ava_let=""
    for l in letters_left:
        if l not in a:
            ava_let+=l
    return ava_let
def get_hint(secret_word,a):
    # import random
    b=[]
    i=0
    while i<len(secret_word):
        let=secret_word[i]
        if let not in a:
            if let not in b:
                b.append(let)
        i=i+1
    return (b[0])
def get_guessed_word(secret_word,a):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in a:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word

def ifvalid(user):
    if len(user)!=1:
        return False
    if not user.isalpha():
        return False
    return True
def play():
    users=input("do u want play_again(y/n):")
    while True:
        if users=="y":
            hangman(secret_word)
            break
        elif users=="n":
            print("thank you for playing.....")
            break
def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("Game levels\n a.Easy\n b.medium\n c.hard\n")
    user=input("enter level u want:")
    if user=="a":
        remain_lives=8
        image_index=[0,1,2,3,4,5,6,7]
    elif user=="b":
        remain_lives=6
        image_index=[0,2,3,5,6,7]
    elif user=="c":
        remain_lives=4
        image_index=[1,3,5,7]

    a=[]
    print(secret_word)
    hint=0
    i=0
    while remain_lives>0:
        ava_letters=get_available_letters(a)
        print("availble letters:",ava_letters)
        guess=input("guess the letter:")
        letter=guess.lower()
        if letter=="hint":
            if hint==0:
                print("your hint of  is:",get_hint(secret_word,a))
                hint=hint+1
            else:
                print("sorry hint alredy used")
        if ifvalid(letter)==False:
            continue
        if letter not in get_available_letters(a):
             continue
        if letter in secret_word:
            a.append(letter)
            print("good guess:",get_guessed_word(secret_word,a))
            print("")
            if is_word_guessed(secret_word, a)==True:
                print( " * * Congratulations, you won! * * ")
                play()
                break
                
        else:
            ava_letters=get_available_letters(a)
            a.append(letter)
            print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, a))
            print(IMAGES[image_index[i]])
            remain_lives-=1
            print("remaing_lives are:",remain_lives)
            i=i+1
        if remain_lives<=0:
            print("you ran out of the process,ur the secret word was",secret_word)
            play()
            break


secret_word = choose_word()

print(len(secret_word))